from typing import List
from clingo import ast

# pylint: disable=all

def atom(location: ast.Location, positive: bool, name: str, arguments: List) -> ast.AST:
    """
    Helper function to create an atom.

    Arguments:
    location --  Location to use.
    positive --  Classical sign of the atom.
    name     --  The name of the atom.
    arguments -- The arguments of the atom.
    """
    ret = ast.Function(location, name, arguments, False)
    if not positive:
        ret = ast.UnaryOperation(location, ast.UnaryOperator.Minus, ret)
    return ast.SymbolicAtom(ret)




