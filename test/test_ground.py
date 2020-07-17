import unittest
import eclingo.main as eclingo
from eclingo.postprocessor.postprocessor import Symbol
from eclingo.postprocessor.postprocessor import EpistemicSign

class TestGroundObjectiveProgramsG91(unittest.TestCase):

    def setUp(self):
        self.eclingo_control = eclingo.Control(max_models=0,
                                                semantics=False,
                                                optimization=eclingo.__optimization__)


    def test_prog_fact(self):
        program = "a."
        self.eclingo_control.add(program)
        self.eclingo_control.parse()
        result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
        self.assertEqual(result, [[]])

    def test_prog_fact2(self):
        program = "a.\nb."
        self.eclingo_control.add(program)
        self.eclingo_control.parse()
        result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
        self.assertEqual(result, [[]])

    def test_prog_fact2_constraint(self):
        program = """a.
        b.
        :- not &k{ a }.
        """
        self.eclingo_control.add(program)
        self.eclingo_control.parse()
        result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
        self.assertEqual(result, [[Symbol('a', [], True, EpistemicSign.NoSign)]])

    def test_prog_fact_show(self):
        program = """a.
        b.
        #show a/0.
        """
        self.eclingo_control.add(program)
        self.eclingo_control.parse()
        result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
        self.assertEqual(result, [[Symbol('a', [], True, EpistemicSign.NoSign)]])