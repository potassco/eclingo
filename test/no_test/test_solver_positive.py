import unittest
from parametrized import ParametrizedTestCase
import eclingo
from eclingo.config import AppConfig
from eclingo.util.logger import silent_logger
from literals import * # pylint: disable=wildcard-import, unused-wildcard-import
# from eclingo.grounder import EpistemicSignature


def append_candidates(obtained_candidates, candidate):
    pos = sorted(candidate[0])
    neg = sorted(candidate[1])
    candidate = (pos, neg)
    obtained_candidates.append(candidate)


class TestSolverPositive(ParametrizedTestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.econtrol = eclingo.Control(control=self.control, config=self.param)
        # self.econtrol.config.eclingo_verbose = 10

    def prepare(self, program):
        self.econtrol.add_program(program)
        self.econtrol.ground()
        self.econtrol.prepare_solver()

    def assert_candidates(self, candidates):
        candidates2 = []
        for candidate in candidates:
            c0 = set(candidate[0])
            c0.difference_update(set(self.econtrol.grounder.epistemic_facts))
            c = (sorted(c0), candidate[1])
            candidates2.append(c)
        candidates = candidates2
        candidates.sort()
        obtained_candidates = []
        for candidate in self.econtrol.solver.generate_candidates():
            append_candidates(obtained_candidates, candidate)
        obtained_candidates.sort()
        self.assertEqual(obtained_candidates, candidates)


    def assert_wv(self, wv, candidates):
        for candidate in wv:
            self.assertTrue(self.econtrol.solver.test_candidate(candidate))
        non_wvs = []
        for candidate in candidates:
            if candidate not in wv:
                non_wvs.append(candidate)
        for candidate in non_wvs:
            self.assertFalse(self.econtrol.solver.test_candidate(candidate))


    def test_fact(self):
        program    = "a."
        candidates = [([], [])]
        self.prepare(program)
        self.assert_candidates(candidates)

    def test_fact_sn(self):
        program = "-a."
        candidates = [([], [])]
        self.prepare(program)
        self.assert_candidates(candidates)


    def test_cycle(self):
        program = """
        a :- not b.
        b :- not a.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assert_candidates(candidates)

    def test_fact_k(self):
        program = """
        a.
        b :- &k{ a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assert_candidates(candidates)


    def test_missing_fact_k(self):
        program = """
        -a.
        b :- &k{ a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assert_candidates(candidates)


    def test_cycle_k(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ a }.
        """
        candidates = [([ka], []), ([], [ka])]
        wvs = [([], [ka])]
        self.prepare(program)
        self.assert_candidates(candidates)
        self.assert_wv(wvs, candidates)


    def test_pseudo_fact_k(self):
        program = """
        {a}.
        :- not a.
        b :- &k{ a }.
        """
        candidates = [([ka], []), ([], [ka])]
        wvs = [([ka], [])]
        self.prepare(program)
        self.assert_candidates(candidates)
        self.assert_wv(wvs, candidates)


def load_tests(_loader, _tests, _pattern):
    default_config = AppConfig()
    project_test_config = AppConfig()
    project_test_config.eclingo_project_test = True

    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestSolverPositive, param=default_config))
    suite.addTest(ParametrizedTestCase.parametrize(TestSolverPositive, param=project_test_config))
    return suite
