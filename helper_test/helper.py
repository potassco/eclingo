import unittest
import clingo as _clingo

from eclingo.util.astutil import ast_repr as _ast_repr

a  = _clingo.Function('a', [], True)
b  = _clingo.Function('b', [], True)
c  = _clingo.Function('c', [], True)
d  = _clingo.Function('d', [], True)
e  = _clingo.Function('e', [], True)
f  = _clingo.Function('f', [], True)

def s_neg(symbol):
    return _clingo.Function(symbol.name, symbol.arguments, False)

class TestHelper(unittest.TestCase):

    def setUp(self):
        self.printing = False
        self.printing_ast_repr = False

    def assert_equal_ordered(self, obj1, obj2):
        obj1 = sorted(obj1)
        obj2 = sorted(obj2)
        self.assertEqual(obj1, obj2)

    def _print(self, result):
        if self.printing:
            print(result)

    def _print_ast(self, result):
        if self.printing or self.printing_ast_repr:
            print(result)
        if self.printing and self.printing_ast_repr:
            print(_ast_repr(result))