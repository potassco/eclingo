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





class TestSolver(ParametrizedTestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.econtrol = eclingo.Control(control=self.control, config=self.param)
        # self.econtrol.config.eclingo_verbose = 10

    def prepare(self, program):
        self.econtrol.add_program(program)
        self.econtrol.ground()
        self.econtrol.prepare_solver()

    def assertCandidates(self, candidates):
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

    def assertWV(self, wv, candidates):
        for candidate in wv:
            self.assertTrue(self.econtrol.solver.test_candidate(candidate))
        non_wvs = []
        for candidate in candidates:
            if candidate not in wv:
                non_wvs.append(candidate)
        for candidate in non_wvs:
            self.assertFalse(self.econtrol.solver.test_candidate(candidate))


    def test_fact_Ksn(self):
        program = """
        -a.
        b :- &k{ -a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_fact_Knot(self):
        program = """
        a.
        b :- &k{ not a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_fact_Knotnot(self):
        program = """
        a.
        b :- &k{ not not a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_fact_Knotnotsn(self):
        program = """
        -a.
        b :- &k{ not not -a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_K(self):
        program = """
        -a.
        b :- &k{ a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_Knot(self):
        program = """
        -a.
        b :- &k{ not a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_Knotnot(self):
        program = """
        -a.
        b :- &k{ not not a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_Ksn(self):
        program = """
        a.
        b :- &k{ -a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_Knotsn(self):
        program = """
        a.
        b :- &k{ not -a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_missing_fact_Knotnotsn(self):
        program = """
        a.
        b :- &k{ not not -a }.
        """
        candidates = [([], [])]
        self.prepare(program)
        self.assertCandidates(candidates)

    def test_cycle_K(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ a }.
        """
        candidates = [([ka], []), ([], [ka])]
        wvs = [([], [ka])]
        self.prepare(program)
        self.assertCandidates(candidates)
        self.assertWV(wvs, candidates)

    def test_cycle_Knot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not a }.
        """
        candidates = [([knota], []), ([], [knota])]
        wvs = [([], [knota])]
        self.prepare(program)
        self.assertCandidates(candidates)
        self.assertWV(wvs, candidates)

    def test_cycle_Knotnot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not not a }.
        """
        candidates = [([knot2a], []), ([], [knot2a])]
        wvs = [([], [knot2a])]
        self.prepare(program)
        self.assertCandidates(candidates)
        self.assertWV(wvs, candidates)

    def test_pseudo_fact_K(self):
        program = """
        {a}.
        :- not a.
        b :- &k{ a }.
        """
        candidates = [([ka], []), ([], [ka])]
        wvs = [([ka], [])]
        self.prepare(program)
        self.assertCandidates(candidates)
        self.assertWV(wvs, candidates)


def load_tests(_loader, _tests, _pattern):
    default_config = AppConfig()
    project_test_config = AppConfig()
    project_test_config.eclingo_project_test = True

    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestSolver, param=default_config))
    suite.addTest(ParametrizedTestCase.parametrize(TestSolver, param=project_test_config))
    return suite
