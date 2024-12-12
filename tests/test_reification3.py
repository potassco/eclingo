import clingox
from clingo.ast import AST
from clingox.ast import theory_term_to_term

from eclingo.parsing.transformers import ast_reify
from tests.test_reification2 import parse_literal, parse_term

from .ast_tester import ASTTestCase


class Test(ASTTestCase):
    def test_theory_atom(self):
        self.assertEqual(
            ast_reify.theory_atom_to_term(parse_literal("&k{ p(X) }")),
            parse_term("k(p(X))"),
        )

        self.assertEqual(
            ast_reify.theory_atom_to_term(parse_literal("&k{ a(Y) }")),
            parse_term("k(a(Y))"),
        )

        self.assertEqual(
            ast_reify.theory_atom_to_term(parse_literal("&k{ b(c) }")),
            parse_term("k(b(c))"),
        )
