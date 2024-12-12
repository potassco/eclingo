import sys
import time
from collections import namedtuple
from typing import Optional, Sequence, cast

import clingo
from clingo import Function, Symbol
from clingo.control import Configuration
from clingox.backend import SymbolicBackend

from eclingo.config import AppConfig

from .candidate import Candidate


def _approximate(
    ctl: clingo.Control,
) -> Optional[tuple[Sequence[Symbol], Sequence[Symbol]]]:
    """
    Approximate the stable models of a program.

    Parameters
    ----------
    ctl
        A control object with a program. Grounding should be performed on this
        control object before calling this function.

    the following must be set before calling this function.
    ctl.configuration.solve.solve_limit = 0

    Returns
    -------
    Returns `None` if the problem is determined unsatisfiable. Otherwise,
    returns an approximation of the stable models of the program in form of a
    pair of sequences of symbols. Atoms contained in the first sequence are
    true and atoms not contained in the second sequence are false in all stable
    models.

    Notes
    -----
    Runs in polynomial time. An approximation might be returned even if the
    problem is unsatisfiable.
    """
    ctl.solve()
    ctl.cleanup()

    # check if the problem is conflicting
    if ctl.is_conflicting:
        return None

    # return approximation
    lower = []
    upper = []
    for sa in ctl.symbolic_atoms:
        upper.append(sa.symbol)
        if sa.is_fact:
            lower.append(sa.symbol)
    return lower, upper


PreprocessingResult = namedtuple(
    "PreprocessingResult",
    [
        "unsatisfiable",
        "lower",
        "upper",
    ],
)

program_meta_encoding = """\
conjunction(B) :- literal_tuple(B),
                        hold(L) : literal_tuple(B,  L), L > 0;
                    not hold(L) : literal_tuple(B, -L), L > 0.

body(normal(B)) :- rule(_, normal(B)), conjunction (B).

body(sum(B, G)) :- rule(_, sum(B,G)),
#sum {
    W,L : hold(L), weighted_literal_tuple(B, L,W), L>0;
    W,L : not hold(L), weighted_literal_tuple(B, -L,W), L>0
} >= G.

hold(A) : atom_tuple(H,A) :- rule(disjunction(H), B), body(B).

{hold(A) : atom_tuple(H,A)} :- rule(choice(H), B), body(B).

atom_map(SA, A) :- output(SA,LT), #count{LL : literal_tuple(LT, LL)} = 1, literal_tuple(LT, A).

strong_negatation_complement(A, B) :- atom_map(u(SA), A), atom_map(u(-SA), B).
:- hold(A), hold(B), strong_negatation_complement(A, B).

symbolic_atom(SA) :- atom_map(SA, _).

symbolic_epistemic_atom(k(A)) :- symbolic_atom(k(A)).
epistemic_atom_map(KSA, KA) :- atom_map(KSA, KA), symbolic_epistemic_atom(KSA).
epistemic_atom_int(KA) :- epistemic_atom_map(_, KA).

symbolic_objective_atom(OSA) :- symbolic_atom(OSA), not symbolic_epistemic_atom(OSA).

has_epistemic_atom(A) :- symbolic_epistemic_atom(k(A)).


fact(SA) :- output(SA, LT), #count {L : literal_tuple(LT, L)} = 0.

hold_symbolic_atom(SA) :- atom_map(SA, A), hold(A).
hold_symbolic_atom(SA) :- fact(SA).

u(SA)    :- fact(u(SA)).
u(SA)    :- output(u(SA), B), conjunction(B).
not1(SA) :- output(not1(SA), B), conjunction(B).
not2(SA) :- output(not2(SA), B), conjunction(B).

{k(A)} :- output(k(A), _).

hold(L) :- k(A), output(k(A), B), literal_tuple(B, L).
:- hold(L) , not k(A), output(k(A), B), literal_tuple(B, L).

preprocessing_hold(KA) :- epistemic_atom_map(k(SA), KA), hold_symbolic_atom(SA).
"""


class CandidateTesterReification:
    def __init__(self, config: AppConfig, reified_program: Sequence[Symbol]):
        self.num_solve_calls = 0
        self._config = config
        self.control = clingo.Control(["0"], message_limit=0)
        self.reified_program = reified_program
        assert isinstance(self.control.configuration.solve, Configuration)
        self.control.configuration.solve.enum_mode = "cautious"

        self.initialized_control = False
        self.grounding_time = 0

        self.unsatisfiable = False
        self.objective_atoms: frozenset[Symbol] = frozenset()
        self.epistemic_atoms: frozenset[Symbol] = frozenset()
        self._epistemic_atoms_int: set[Symbol] = set()

    def _initialize_control(self):
        start_time = time.time()
        with SymbolicBackend(self.control.backend()) as backend:
            for symbol in self.reified_program:
                backend.add_rule([symbol])
        self.control.add("base", [], program_meta_encoding)
        self.control.ground([("base", [])])
        self.initialized_control = True
        self.grounding_time += time.time() - start_time

    def __call__(self, candidate: Candidate) -> bool:
        candidate_pos = []  # rename as query_pos
        candidate_neg = []
        candidate_assumptions = []

        for literal in candidate.pos:
            assumption = (literal, True)
            candidate_assumptions.append(assumption)
            literal = literal.arguments[0]
            candidate_pos.append(literal)

        for literal in candidate.extra_assumptions.pos:
            assumption = (literal, True)
            candidate_assumptions.append(assumption)

        for literal in candidate.neg:
            assumption = (literal, False)
            candidate_assumptions.append(assumption)
            literal = literal.arguments[0]
            candidate_neg.append(literal)

        for literal in candidate.extra_assumptions.neg:
            assumption = (literal, False)
            candidate_assumptions.append(assumption)

        assert isinstance(self.control.configuration.solve, Configuration)
        self.control.configuration.solve.models = 0
        self.control.configuration.solve.project = "no"

        if not self.initialized_control:
            self._initialize_control()

        with cast(
            clingo.SolveHandle,
            self.control.solve(yield_=True, assumptions=candidate_assumptions),
        ) as handle:
            model = None
            for model in handle:
                self.num_solve_calls += 1
                for atom in candidate_pos:
                    if not model.contains(atom):
                        return False

            assert model is not None, str(candidate)

            for atom in candidate_neg:
                if model.contains(atom):
                    return False
        return True

    # def basic_preprocessing(self) -> PreprocessingResult:
    #     solve_limit = self.control.configuration.solve.solve_limit
    #     self.control.configuration.solve.solve_limit = 0
    #     ret = self._basic_preprocessing()
    #     self.control.configuration.solve.solve_limit = solve_limit
    #     return ret

    def _basic_preprocessing(self) -> PreprocessingResult:
        ret = _approximate(self.control)
        if ret is None:
            return PreprocessingResult(unsatisfiable=True, lower=[], upper=[])
        lower_all, upper_all = ret
        lower, upper = self._prepreocessing_atoms(lower_all, upper_all)
        self.objective_atoms = frozenset(
            e.arguments[0] for e in upper_all if e.name == "symbolic_objective_atom"
        )
        self.epistemic_atoms = frozenset(
            e.arguments[0] for e in upper_all if e.name == "has_epistemic_atom"
        )
        self._epistemic_atoms_int = set(
            e.arguments[0] for e in upper_all if e.name == "epistemic_atom_int"
        )
        # print(f"\n\nupper_all: {' '.join(sorted(str(a) for a in upper_all if a.name=='atom_map'))}")
        return PreprocessingResult(unsatisfiable=False, lower=lower, upper=upper)

    def _prepreocessing_atoms(self, lower, upper):
        lower = frozenset(
            e.arguments[0] for e in lower if e.name == "preprocessing_hold"
        )
        upper = frozenset(
            e.arguments[0] for e in upper if e.name == "preprocessing_hold"
        )
        return lower, upper

    def fast_preprocessing(self) -> PreprocessingResult:
        if not self.initialized_control:
            self._initialize_control()
        ret = self._fast_preprocessing()
        unsatisfiable, lower, upper = ret
        names = {"u", "k", "not1", "not2"}
        lower = [e for e in lower if e.name in names]
        upper = [e for e in upper if e.name in names]
        return PreprocessingResult(unsatisfiable, lower, upper)

    def _fast_preprocessing(self) -> PreprocessingResult:
        # print("*" * 50)
        assert isinstance(self.control.configuration.solve, Configuration)
        solve_limit = self.control.configuration.solve.solve_limit
        self.control.configuration.solve.solve_limit = 0

        basic_preprocessing_info = self._basic_preprocessing()
        if basic_preprocessing_info.unsatisfiable:
            ret = basic_preprocessing_info
        else:
            ret = self._fast_preprocessing_loop(
                basic_preprocessing_info.lower, basic_preprocessing_info.upper
            )

        self.control.configuration.solve.solve_limit = solve_limit
        return ret

    def _fast_preprocessing_loop(self, lower, upper) -> PreprocessingResult:
        lower_size, upper_size = len(lower), len(upper)
        prev_lower: frozenset[Symbol] = frozenset()
        lower_prev_size, upper_prev_size = 0, sys.maxsize
        # print(f"{lower_prev_size} {lower_size} {upper_prev_size} {upper_size}")
        while lower_prev_size < lower_size or upper_prev_size > upper_size:
            # print("*" * 50)
            # print(f"lower: {lower}")
            # print(f"upper: {upper}")
            new_rules = []
            if lower_prev_size < lower_size:
                new_rules.extend(self._fast_preprocessing_lower(lower, prev_lower))
                prev_lower = lower

            if upper_prev_size > upper_size:
                new_rules.extend(self._fast_preprocessing_upper(upper))

            with SymbolicBackend(self.control.backend()) as symbolic_backend:
                for rule in new_rules:
                    symbolic_backend.add_rule(*rule)

            ret = _approximate(self.control)
            if ret is None:
                break
            lower_all, upper_all = ret
            lower, upper = self._prepreocessing_atoms(lower_all, upper_all)
            lower_prev_size, upper_prev_size = lower_size, upper_size
            lower_size, upper_size = len(lower), len(upper)

        if ret is None:
            return PreprocessingResult(unsatisfiable=True, lower=[], upper=[])
        return PreprocessingResult(
            unsatisfiable=False, lower=lower_all, upper=upper_all
        )

    def _fast_preprocessing_lower(self, lower, prev_lower):
        lower_diff = lower.difference(prev_lower)
        for atom in lower_diff:
            yield ([], [], [Function("hold", [atom])])

    def _fast_preprocessing_upper(self, upper):
        remove_from_epistemic_atoms_int = []
        for atom in self._epistemic_atoms_int:
            if atom not in upper:
                remove_from_epistemic_atoms_int.append(atom)
                yield ([], [Function("hold", [atom])], [])
        self._epistemic_atoms_int.difference_update(remove_from_epistemic_atoms_int)
