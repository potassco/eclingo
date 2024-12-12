import unittest

from clingo import Function
from clingo.ast import Sign

from eclingo.literals import Literal


class Test(unittest.TestCase):
    def assert_str(self, literal: Literal, s: str) -> None:
        self.assertEqual(str(literal), s)

    def test_str(self):
        symbol = Function("a")
        self.assert_str(Literal(symbol, Sign.NoSign), "a")
        self.assert_str(Literal(symbol, Sign.Negation), "not a")
        self.assert_str(Literal(symbol, Sign.DoubleNegation), "not not a")

    def assert_repr(self, literal: Literal, s: str) -> None:
        self.assertEqual(repr(literal), s)

    def test_repr(self):
        symbol = Function("a")
        s = repr(symbol)
        self.assert_repr(Literal(symbol, Sign.NoSign), repr(Sign.NoSign) + s)
        self.assert_repr(Literal(symbol, Sign.Negation), repr(Sign.Negation) + s)
        self.assert_repr(
            Literal(symbol, Sign.DoubleNegation), repr(Sign.DoubleNegation) + s
        )
