"""
This module contains functions for reififcation of `AST` objects
"""

import clingo
from clingo import ast
from clingo.ast import AST, ASTType, Sign
from clingox.ast import theory_term_to_literal, theory_term_to_term


def _positive_symbolic_literal_to_term(x: AST):
    """
    Helper function to ensure proper treatment of clingo.Function and ast.Function
    """
    if x.ast_type != ast.ASTType.Function or x.arguments or x.external:
        return x
    return ast.SymbolicTerm(x.location, clingo.Function(x.name, [], True))


def theory_atom_to_term(x: AST) -> AST:
    """
    Convert the given literal into ast.Function
    - `x.atom.term` -> subjective literal term
    - `x.atom.elements[0] -> AST of type TheoryAtomElements that is
    assumed as one TheoryAtomElement with unique term and empty condition

    Parameters
    ----------
    x
        An `AST` that represents a literal to be converted into theory term to term.

    Returns
    -------
    An `AST` that represnts the reified Theory Atom Element as an AST.Function.
    """
    if x.atom.elements[0].terms[0].ast_type == ASTType.TheoryUnparsedTerm:
        literal = theory_term_to_literal(x.atom.elements[0].terms[0])
        term = symbolic_literal_to_term(literal)

    else:
        term = x.atom.elements[0].terms[0]
        term = theory_term_to_term(term, False)

    return ast.Function(x.location, str(x.atom.term), [term], False)


def symbolic_literal_to_term(
    lit: AST, negation_name: str = "not1", double_negation_name: str = "not2"
) -> AST:
    """
    Convert the given literal into a clingo term according to the following rules:
    - `atom => atom`
    - `not atom => not1(atom)`
    - `not not atom => not2(atom)`

    Parameters
    ----------
    lit
        An `AST` that represents a literal.
    negation_name
        A string to be used to represent negation.
    double_negation_name
        A string to be used to represent double negation.

    Returns
    -------
    An `AST` that represnts the reified literal as a term.
    """
    assert lit.ast_type == ASTType.Literal
    if lit.atom.ast_type != ASTType.SymbolicAtom:
        return lit
    symbol = lit.atom.symbol

    if lit.atom.symbol.ast_type == ASTType.UnaryOperation:
        symbol = symbol.argument

    symbol = _positive_symbolic_literal_to_term(symbol)

    if lit.atom.symbol.ast_type == ASTType.UnaryOperation:
        symbol = ast.UnaryOperation(lit.location, 0, symbol)

    if lit.sign == ast.Sign.NoSign:
        return symbol

    sign_name = negation_name if lit.sign == Sign.Negation else double_negation_name

    return ast.Function(lit.location, sign_name, [symbol], False)


def reification_program_to_str(program):  # pragma: no cover
    """
    Helper function to convert a reified fact program into a string.
    """
    prg_string = []
    for e1 in program:
        prg_string.append(str(e1))

    program = ". ".join(prg_string)
    program = program + "."
    return program


def program_to_str(program):
    """
    Helper function to parse a given program into string.
    """
    prg_string = []
    for e1 in program:
        prg_string.append(str(e1))

    program = " ".join(prg_string)
    return program
