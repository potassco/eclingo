"""Module providing an AST function Trasnformer"""

import clingo
from clingo import ast
from clingo.ast import AST, Transformer


def rule_to_symbolic_term_adapter(x: AST):
    """
    Replaces all occurrences of objects of the class clingo.Function in x
    by the corresponding object of the class ast.Function. It takes care of
    ajust the ast removing the SymbolicTerm object if necessary.
    """
    return _SymbolicTermToFunctionTransformer().visit(x)


class _SymbolicTermToFunctionTransformer(Transformer):
    """Transforms a SymbolicTerm AST into a Function AST"""

    def visit_SymbolicTerm(self, term: AST):  # pylint: disable=invalid-name
        """
        Transform the given symbolic term.

        Parameters
        ----------
        x
            The AST to rewrite.

        Returns
        -------
        The rewritten AST.
        """

        symbol = term.symbol

        if symbol.type != clingo.SymbolType.Function:
            return term

        location = term.location
        name = symbol.name
        arguments = symbol.arguments

        return ast.Function(location, name, arguments, False)
