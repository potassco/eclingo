from clingo import ast as _ast

# pylint: disable=all

class ASTInspector(object):
    """
    Visit `clingo.clingo.ast.AST` objects by visiting all child nodes.

    Implement `visit_<type>` where `<type>` is the type of the nodes to be
    visited.
    """
    def __init__(self):
        self.level = 0
        self.string = ""

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
            ident = 2*self.level*" "
            self.string += ident + str(x.type) + ":    " + str(x) + "\n"
            self.level += 1
            self.visit_children(x, *args, **kwargs)
            self.level -= 1
            return
        if isinstance(x, list):
            return self.visit_list(x, *args, **kwargs)
        if isinstance(x, tuple):
            return self.visit_tuple(x, *args, **kwargs)
        if x is None:
            return self.visit_none(x, *args, **kwargs)
        raise TypeError("unexpected type: {}".format(x))

def inspect_ast(stm):
    t = ASTInspector()
    t.visit(stm)
    return t.string