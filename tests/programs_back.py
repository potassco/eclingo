import subprocess
from collections import namedtuple
from dataclasses import dataclass
from typing import Iterable, List

import clingo
import clingox
from clingo import Function
from clingox.testing.ast import parse_term

from eclingo.solver.candidate import Candidate


def _ast_to_symbol(x: clingo.ast.AST) -> clingo.Symbol:
    """
    Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function.
    """
    if x.ast_type == clingo.ast.ASTType.SymbolicTerm:
        return x.symbol
    if x.ast_type != clingo.ast.ASTType.Function:
        return x
    return clingo.symbol.Function(
        x.name,
        [_ast_to_symbol(a) for a in x.arguments],
        positive=True,
    )


class ASTtoSymbol(clingo.ast.Transformer):
    """Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function."""

    def visit_Function(self, x: clingo.ast.AST):  # pylint: disable=invalid-name
        """
        Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function.
        """
        return _ast_to_symbol(x)


def build_candidate_atom(atom: clingo.ast.AST) -> clingo.symbol.Symbol:
    ast_to_symbol = ASTtoSymbol()
    atom = ast_to_symbol(atom)
    atom = clingo.symbol.Function("u", [atom.arguments[0]], True)
    return clingo.symbol.Function("k", [atom], True)


@dataclass
class Program:
    program: str
    unoptimiced_candidates: List[Candidate]
    candidates: List[Candidate]
    wv_candidates: List[Candidate]
    non_ground_reifications: str
    description: str = ""

    def __init__(
        self,
        program: str,
        unoptimiced_candidates: List[Candidate] = None,
        candidates: str = None,
        wv_candidates: List[Candidate] = None,
        non_ground_reifications: str = None,
        description: str = "",
    ) -> None:
        self.program = program
        self.unoptimiced_candidates = unoptimiced_candidates
        self.candidates = self.build_candidates(candidates)
        self.wv_candidates = wv_candidates
        self.non_ground_reifications = non_ground_reifications
        if self.non_ground_reifications is None:
            self.ground_reification = None
        else:
            self.ground_reification = subprocess.check_output(
                f'echo "{self.non_ground_reifications}" | clingo --output=reify',
                shell=True,
            )
            self.ground_reification = self.ground_reification.decode("utf-8")
        self.description = description

    def build_candidate(self, candidate: str) -> Candidate:
        atoms = candidate.split(" ")
        atoms = [parse_term(atom) for atom in atoms]
        pos = [build_candidate_atom(atom) for atom in atoms if atom.name == "k"]
        neg = [
            build_candidate_atom(atom.arguments[0])
            for atom in atoms
            if atom.name == "not1"
        ]
        return Candidate(pos=pos, neg=neg)

    def build_candidates(self, candidate: Iterable[str]) -> List[Candidate]:
        return [self.build_candidate(c) for c in candidate]


programs = [
    Program(
        description="",
        program="a. b :- &k{a}.",
        non_ground_reifications="u(a). u(b) :- k(u(a)). { k(u(a)) } :- u(a).",
        unoptimiced_candidates=[
            "k(a)",
            "not1(k(a))",
        ],
        candidates=[
            "k(a)",
        ],
    ),
    Program(
        description="",
        program="{a}. b :- &k{a}.",
        non_ground_reifications="{u(a)}. u(b) :- k(u(a)). { k(u(a)) } :- u(a).",
        unoptimiced_candidates=[
            "k(a)",
            "not1(k(a))",
        ],
        candidates=[
            "k(a)",
            "not1(k(a))",
        ],
    ),
]
