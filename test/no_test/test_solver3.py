import unittest
import eclingo
from literals import *
from eclingo.util.logger import silent_logger
# from eclingo.grounder import EpistemicSignature


def append_wvs(obtained_wvs, candidate):
    pos = sorted(candidate[0])
    neg = sorted(candidate[1])
    candidate = (pos, neg)
    obtained_wvs.append(candidate)

class TestControl3(unittest.TestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.econtrol = eclingo.control.Control(control=self.control)
        # self.econtrol.config.eclingo_verbose = 10

    def prepare(self, program):
        self.econtrol.add_program(program)
        self.econtrol.ground()
        self.econtrol.prepare_solver()

    def assertWV(self, wvs):
        wvs2 = []
        for wv in wvs:
            wv0 = set(wv[0])
            wv0.difference_update(set(self.econtrol.grounder.epistemic_facts))
            wv = (sorted(wv0), wv[1])
            wvs2.append(wv)
        wvs = wvs2
        wvs.sort()
        obtained_wvs = [wv for wv in self.econtrol.solver.solve()]
        for wv in obtained_wvs:
            wv[0].sort()
            wv[1].sort()
        obtained_wvs.sort()
        self.assertEqual(wvs, obtained_wvs)


    def test_fact_Ksn(self):
        program = """
        -a.
        b :- &k{ -a }.
        :- not b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Ksn2(self):
        program = """
        -a.
        b :- &k{ -a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knot(self):
        program = """
        a.
        b :- &k{ not a }.
        :- b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knot2(self):
        program = """
        a.
        b :- &k{ not a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotsn(self):
        program = """
        -a.
        b :- &k{ not -a }.
        :- b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotsn2(self):
        program = """
        -a.
        b :- &k{ not -a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotnot(self):
        program = """
        a.
        b :- &k{ not not a }.
        :- not b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotnot2(self):
        program = """
        a.
        b :- &k{ not not a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotnotsn(self):
        program = """
        -a.
        b :- &k{ not not -a }.
        :- not b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_fact_Knotnotsn2(self):
        program = """
        -a.
        b :- &k{ not not -a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knot(self):
        program = """
        -a.
        b :- &k{ not a }.
        :- not b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knot2(self):
        program = """
        -a.
        b :- &k{ not a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knot2(self):
        program = """
        -a.
        b :- &k{ not a }.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotnot(self):
        program = """
        -a.
        b :- &k{ not not a }.
        :- b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotnot2(self):
        program = """
        -a.
        b :- &k{ not not a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Ksn(self):
        program = """
        a.
        b :- &k{ -a }.
        :- b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Ksn2(self):
        program = """
        a.
        b :- &k{ -a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotsn(self):
        program = """
        a.
        b :- &k{ not -a }.
        :- not b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotsn2(self):
        program = """
        a.
        b :- &k{ not -a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotnotsn(self):
        program = """
        a.
        b :- &k{ not not -a }.
        :- b.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_missing_fact_Knotnotsn2(self):
        program = """
        a.
        b :- &k{ not not -a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

   

    def test_cycle_Knot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not a }.
        :- b.
        """
        wvs = [([], [knota])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_Knot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_Knotnot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not not a }.
        :- b.
        """
        wvs = [([], [knot2a])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_Knotnot2(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not not a }.
        :- not b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)



    def test_cycle_notK(self):
        program = """
        a :- not c.
        c :- not a.
        b :- not &k{ a }.
        :- not b.
        """
        wvs = [([], [ka])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_notK2(self):
        program = """
        a :- not c.
        c :- not a.
        b :- not &k{ a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_notKnot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- not &k{ not a }.
        :- not b.
        """
        wvs = [([], [knota])]
        self.prepare(program)
        self.assertWV(wvs)

    def test_cycle_notKnot2(self):
        program = """
        a :- not c.
        c :- not a.
        b :- not &k{ not a }.
        :- b.
        """
        wvs = []
        self.prepare(program)
        self.assertWV(wvs)





