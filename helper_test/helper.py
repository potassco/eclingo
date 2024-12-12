import unittest


class TestHelper(unittest.TestCase):
    def setUp(self):
        self.printing = False
        self.printing_ast_repr = False

    def assert_equal_ordered(self, obj1, obj2):
        obj1 = sorted(obj1)
        obj2 = sorted(obj2)
        self.assertEqual(str(obj1), str(obj2))
        self.assertEqual(obj1, obj2)
