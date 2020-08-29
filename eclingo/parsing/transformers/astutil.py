from typing import List
from clingo import ast as _ast

# pylint: disable=all

def atom(location: dict, positive: bool, name: str, arguments: List) -> _ast.AST:
    """
    Helper function to create an atom.

    Arguments:
    location --  Location to use.
    positive --  Classical sign of the atom.
    name     --  The name of the atom.
    arguments -- The arguments of the atom.
    """
    ret = _ast.Function(location, name, arguments, False)
    if not positive:
        ret = _ast.UnaryOperation(location, _ast.UnaryOperator.Minus, ret)
    return _ast.SymbolicAtom(ret)


class Visitor(object):
    """
    Visit `clingo.ast.AST` objects by visiting all child nodes.

    Implement `visit_<type>` where `<type>` is the type of the nodes to be
    visited.
    """
    def visit_children(self, x, *args, **kwargs):
        """
        Visit all child nodes of the current node.
        """
        for key in x.child_keys:
            self.visit(getattr(x, key), *args, **kwargs)

    def visit_list(self, x, *args, **kwargs):
        """
        Visit a list of AST nodes.
        """
        for y in x:
            self.visit(y, *args, **kwargs) 

    def visit_tuple(self, x, *args, **kwargs):
        """
        Visit a list of AST nodes.
        """
        for y in x:
            self.visit(y, *args, **kwargs)

    def visit_none(self, *args, **kwargs):
        """
        Visit none.

        This, is to handle optional arguments that do not have a visit method.
        """

    def visit(self, x, *args, **kwargs):
        """
        Default visit method to dispatch calls to child nodes.
        """
        if isinstance(x, _ast.AST):
            attr = "visit_" + str(x.type)
            if hasattr(self, attr):
                return getattr(self, attr)(x, *args, **kwargs)
            return self.visit_children(x, *args, **kwargs)
        if isinstance(x, list):
            return self.visit_list(x, *args, **kwargs)
        if isinstance(x, tuple):
            return self.visit_tuple(x, *args, **kwargs)
        if x is None:
            return self.visit_none(x, *args, **kwargs)
        raise TypeError("unexpected type: {}".format(x))

    def __call__(self, x, *args, **kwargs):
        """
        Alternative way to call visit.
        """
        return self.visit(x, *args, **kwargs)


class SignatureVisitor(Visitor):

    def __init__(self):
        self.signature = None

    def visit_Symbol(self, stm):
        self.signature = (stm.name, 0)

    def visit_Function(self, stm):
        self.signature = (stm.name, len(stm.arguments))


def signature(stm):
    t = SignatureVisitor()
    t.visit(stm)
    return t.signature



