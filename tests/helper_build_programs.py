import os
import pprint
import subprocess
import textwrap
from collections import namedtuple
from dataclasses import dataclass
from io import StringIO
from pprint import pformat
from typing import Iterable, List, NamedTuple, Optional, Tuple, Union

import clingo
from clingo import Function, Symbol
from clingox.testing.ast import parse_term

from eclingo.solver.candidate import Assumptions, Candidate


def _ast_to_symbol(x: clingo.ast.AST) -> clingo.Symbol:
    """
    Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function.
    """
    if x.ast_type == clingo.ast.ASTType.SymbolicTerm:
        return x.symbol
    if x.ast_type == clingo.ast.ASTType.UnaryOperation:
        a = _ast_to_symbol(x.argument)
        return clingo.symbol.Function(
            a.name,
            a.arguments,
            positive=not a.positive,
        )
    if x.ast_type != clingo.ast.ASTType.Function:
        return x
    return clingo.symbol.Function(
        x.name,
        [_ast_to_symbol(a) for a in x.arguments],
        positive=True,
    )


class ASTtoSymbol(clingo.ast.Transformer):
    """Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function."""

    def visit_SymbolicTerm(self, x: clingo.ast.AST):  # pylint: disable=invalid-name
        return _ast_to_symbol(x)

    def visit_Function(self, x: clingo.ast.AST):  # pylint: disable=invalid-name
        """
        Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function.
        """
        return _ast_to_symbol(x)

    def visit_UnaryOperation(self, x: clingo.ast.AST):  # pylint: disable=invalid-name
        """
        Transforms a SymbolicTerm AST of type Function into an AST of type ast.Function.
        """
        return _ast_to_symbol(x)


ast_to_symbol = ASTtoSymbol()


def build_objective_atom(atom: clingo.ast.AST) -> clingo.symbol.Symbol:
    if atom.name == "not1":
        return clingo.symbol.Function(
            "not1", [clingo.symbol.Function("u", [atom.arguments[0]])]
        )
    return clingo.symbol.Function("u", [atom])


def build_subjective_atom(atom: clingo.ast.AST) -> clingo.symbol.Symbol:
    atom = build_objective_atom(atom.arguments[0])
    return clingo.symbol.Function("k", [atom])


def build_atom(atom: clingo.ast.AST) -> clingo.symbol.Symbol:
    if atom.name == "k":
        return build_subjective_atom(atom)
    return build_objective_atom(atom)


def build_candidate_without_assumptions(candidate: str, assumptions=None) -> Candidate:
    candidate = candidate.strip()
    if not candidate:
        return Candidate(pos=[], neg=[])
    atoms = candidate.split(" ")
    atoms = [atom.strip() for atom in atoms if atom]
    atoms = [parse_term(atom) for atom in atoms]
    atoms = [ast_to_symbol(atom) for atom in atoms]
    pos = [build_subjective_atom(atom) for atom in atoms if atom.name != "no"]
    neg = [
        build_subjective_atom(atom.arguments[0]) for atom in atoms if atom.name == "no"
    ]
    if assumptions is not None:
        return Candidate(pos=pos, neg=neg, extra_assumptions=assumptions)
    return Candidate(pos=pos, neg=neg)


def build_assumptions(assumptions: str) -> Assumptions:
    if not assumptions:
        return Assumptions(pos=[], neg=[])
    atoms = assumptions.split(" ")
    atoms = [ast_to_symbol(parse_term(atom)) for atom in atoms]
    pos = [build_objective_atom(atom) for atom in atoms if atom.name != "no"]
    neg = [
        build_objective_atom(atom.arguments[0]) for atom in atoms if atom.name == "no"
    ]
    return Assumptions(pos=pos, neg=neg)


def build_candidate(
    candidate: Union[str, Tuple[str, str]]
) -> Optional[List[Candidate]]:
    if isinstance(candidate, str):
        return build_candidate_without_assumptions(candidate)
    assumptions = build_assumptions(candidate[1])
    return build_candidate_without_assumptions(candidate[0], assumptions)


def build_candidates(candidates: Optional[Iterable[str]]) -> Optional[List[Candidate]]:
    if candidates is None:
        return None
    return [build_candidate(c) for c in candidates]
