import itertools
from typing import Dict, Iterator

from clingo import Symbol, SymbolicAtom

from eclingo import internal_states
from eclingo.prefixes import not_symbol
from eclingo.solver.candidate import Candidate
from eclingo.util import clingoext

from .candidate import Candidate
from .world_view import EpistemicLiteral, WorldView


class WorldWiewBuilder():

    def __init__(self, control: internal_states.InternalStateControl):
        self._epistemic_show_pos_mapping: Dict[Symbol, EpistemicLiteral] = control.show_mapping.positive
        self._epistemic_show_neg_mapping: Dict[Symbol, EpistemicLiteral] = control.show_mapping.negative

    def __call__(self, candidate: Candidate):
        return self.world_view_from_candidate(candidate)

    def world_view_from_candidate(self, candidate: Candidate):
        epistemic_literals = []
        processed_symbols = []
        for epistemic_literal in candidate.pos:
            if epistemic_literal in self._epistemic_show_pos_mapping:
                show_literal = self._epistemic_show_pos_mapping[epistemic_literal]
                epistemic_literals.append(show_literal)
                processed_symbols.append(show_literal.objective_literal)

        processed_symbols_set = frozenset(processed_symbols)

        for epistemic_literal in candidate.neg:
            if epistemic_literal in self._epistemic_show_neg_mapping:
                show_literal = self._epistemic_show_neg_mapping[epistemic_literal]
                if show_literal.objective_literal not in processed_symbols_set:
                    epistemic_literals.append(show_literal)

        return WorldView(epistemic_literals)


class WorldWiewBuilderWithShow(WorldWiewBuilder):

    def __init__(self, control: internal_states.InternalStateControl):
        super().__init__(control)
        self.control = self._generate_control_show(control)

    def _generate_control_show(self, control: internal_states.InternalStateControl) -> clingoext.Control:
        control_show = clingoext.Control(['0'], message_limit=0)
        control.add_to(control_show)
        self._add_rules_for_negative_check(control_show, control.show_symbolic_atoms())
        control_show.control.configuration.solve.enum_mode = 'cautious' # type: ignore
        return control_show

    def _add_rules_for_negative_check(self, control_show: clingoext.Control, symbolic_show_atoms: Iterator[SymbolicAtom]) -> None:
        """
        adds a rule of the form 'not_u_a :- not u_a' for each symbolic atom 'u_a' in symbolic_show_atoms
        """
        with control_show.symbolic_backend() as backend:
            for symbolic_atom in symbolic_show_atoms:
                if not symbolic_atom.is_fact:
                    symbolic_atom_not = not_symbol(symbolic_atom.symbol)
                    backend.add_rule([symbolic_atom_not], [], [symbolic_atom.symbol], False)


    def world_view_from_candidate(self, candidate: Candidate):
        candidate_assumptions = []
        for literal in candidate[0]:
            assumption = (literal, True)
            candidate_assumptions.append(assumption)
        for literal in candidate[1]:
            assumption = (literal, False)
            candidate_assumptions.append(assumption)
        self.control.configuration.solve.models  = 0
        self.control.configuration.solve.project = "no"

        new_candidate_pos = []
        new_candidate_neg = []
        with self.control.solve(yield_=True, assumptions=candidate_assumptions) as handle:
            model = None
            for model in handle:
                pass

            if model is None:
                raise RuntimeError("Program is unsatisfiable.")

            for symbol in itertools.chain(self._epistemic_show_pos_mapping, self._epistemic_show_neg_mapping):
                if model.contains(symbol):
                    new_candidate_pos.append(symbol)
                else:
                    new_candidate_neg.append(symbol)

        return super().world_view_from_candidate(Candidate(new_candidate_pos, new_candidate_neg, [], []))
