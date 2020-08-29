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


class TestControlPositive2(unittest.TestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.econtrol = eclingo.Control(control=self.control)
        # self.econtrol.config.eclingo_verbose = 10

    def prepare(self, program):
        self.econtrol.add_program(program)
        self.econtrol.ground()
        self.econtrol.prepare_solver()

    def assert_wv(self, wvs):
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


    def test_fact(self):
        program    = "a."
        wvs = [([], [])]
        self.prepare(program)
        self.assert_wv(wvs)

    def test_fact_sn(self):
        program = "-a."
        wvs = [([], [])]
        self.prepare(program)
        self.assert_wv(wvs)


    def test_cycle(self):
        program = """
        a :- not b.
        b :- not a.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assert_wv(wvs)

    def test_fact_k(self):
        program = """
        a.
        b :- &k{ a }.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assert_wv(wvs)


    def test_missing_fact_k(self):
        program = """
        -a.
        b :- &k{ a }.
        """
        wvs = [([], [])]
        self.prepare(program)
        self.assert_wv(wvs)


    def test_cycle_k(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ a }.
        """
        wvs = [([], [ka])]
        self.prepare(program)
        self.assert_wv(wvs)


    def test_pseudo_fact_k(self):
        program = """
        {a}.
        :- not a.
        b :- &k{ a }.
        """
        wvs = [([ka], [])]
        self.prepare(program)
        self.assert_wv(wvs)
