import unittest
import eclingo
from eclingo.parsing import ECLINGO_PREFIX, ECLINGO_PREFIX_K, ECLINGO_PREFIX_NOT
import clingo
# from eclingo.postprocessor.postprocessor import Symbol
# from eclingo.postprocessor.postprocessor import EpistemicSign

a  = clingo.Function('a', [], True)
b  = clingo.Function('b', [], True)
c  = clingo.Function('c', [], True)
d  = clingo.Function('d', [], True)
e  = clingo.Function('e', [], True)
f  = clingo.Function('f', [], True)

ka = clingo.Function(ECLINGO_PREFIX_K + 'a', [], True)
kb = clingo.Function(ECLINGO_PREFIX_K + 'b', [], True)
kc = clingo.Function(ECLINGO_PREFIX_K + 'c', [], True)
kd = clingo.Function(ECLINGO_PREFIX_K + 'd', [], True)
ke = clingo.Function(ECLINGO_PREFIX_K + 'e', [], True)
kf = clingo.Function(ECLINGO_PREFIX_K + 'f', [], True)

nota  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'a', [], True)
notb  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'b', [], True)
notc  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'c', [], True)
notd  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'd', [], True)
note  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'e', [], True)
notf  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'f', [], True)


knota = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'a', [], True)
knotb = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'b', [], True)
knotc = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'c', [], True)
knotd = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'd', [], True)
knote = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'e', [], True)
knotf = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'f', [], True)

class TestGroundObjectiveProgramsG91(unittest.TestCase):



    def setUp(self):
        self.eclingo_control = eclingo.Control()


    def test_prog_fact(self):
        program = "a."
        facts   = sorted([a])
        self.eclingo_control.add(program)
        self.eclingo_control.prepare_solver()
        self.assertEqual(sorted(self.eclingo_control.facts), facts)

    def test_prog_cycle(self):
        program = """
        a.
        b.
        c :- not d.
        d :- not c."""
        facts   = sorted([a, b])
        self.eclingo_control.add(program)
        self.eclingo_control.prepare_solver()
        self.assertEqual(sorted(self.eclingo_control.facts), facts)

    def test_prog_cycle_epistemic(self):
        program = """
        a.
        b.
        c :- not d.
        d :- not c.
        e :- &k{ a }.
        f :- &k{ c }."""
        facts   = sorted([a, b])
        e_facts = sorted([ka])

        self.eclingo_control.add(program)
        self.eclingo_control.prepare_solver()
        self.assertEqual(sorted(self.eclingo_control.facts), facts)
        self.assertEqual(sorted(self.eclingo_control.epistemic_facts), e_facts)
        c_code  = self.eclingo_control.symbol_to_atom[c]
        kc_code = self.eclingo_control.symbol_to_atom[kc]
        candidates = sorted([[-kc_code], [kc_code]])
        self.assertEqual(self.eclingo_control.epistemic_to_atom[kc_code], c_code)
        self.assertEqual(sorted(list(self.eclingo_control.solver.generate_candidate())), candidates)
        self.assertTrue(self.eclingo_control.solver.test_candidate([-kc_code]))
        self.assertFalse(self.eclingo_control.solver.test_candidate([kc_code]))
        self.assertEqual(list(self.eclingo_control.solver.solve()), [[-kc_code]])


    def test_prog_cycle_epistemic_M(self):
        program = """
        a.
        b.
        c :- not d.
        d :- not c.
        e :- not &k{ a }.
        f :- not &k{ not c }."""
        facts   = sorted([a, b])
        e_facts = sorted([ka])

        self.eclingo_control.add(program)
        self.eclingo_control.prepare_solver()
        self.assertEqual(sorted(self.eclingo_control.facts), facts)
        self.assertEqual(sorted(self.eclingo_control.epistemic_facts), e_facts)
        notc_code  = self.eclingo_control.symbol_to_atom[notc]
        knotc_code = self.eclingo_control.symbol_to_atom[knotc]
        candidates = sorted([[-knotc_code], [knotc_code]])
        self.assertEqual(self.eclingo_control.epistemic_to_atom[knotc_code], notc_code)
        self.assertEqual(sorted(list(self.eclingo_control.solver.generate_candidate())), candidates)
        self.assertTrue(self.eclingo_control.solver.test_candidate([-knotc_code]))
        self.assertFalse(self.eclingo_control.solver.test_candidate([knotc_code]))
        self.assertEqual(list(self.eclingo_control.solver.solve()), [[-knotc_code]])
        # print(list(self.eclingo_control.solver.solve()))


    # def test_prog_fact2_constraint(self):
    #     program = """a.
    #     b.
    #     :- not &k{ a }.
    #     """
    #     self.eclingo_control.add(program)
    #     self.eclingo_control.parse()
    #     result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
    #     self.assertEqual(result, [[Symbol('a', [], True, EpistemicSign.NoSign)]])

    # def test_prog_fact_show(self):
    #     program = """a.
    #     b.
    #     #show a/0.
    #     """
    #     self.eclingo_control.add(program)
    #     self.eclingo_control.parse()
    #     result = [sorted(model.symbols) for model in self.eclingo_control.solve()]
    #     self.assertEqual(result, [[Symbol('a', [], True, EpistemicSign.NoSign)]])