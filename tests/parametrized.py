import unittest


class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName="TestSolver", param=None):
        super().__init__(methodName)
        self.param = param
