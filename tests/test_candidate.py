from unittest import TestCase

from eclingo.solver.candidate import Candidate
from tests.helper_build_programs import build_candidate


class TestCandidate(TestCase):
    """
    Test the Candidate class.
    """

    def test_candidate_prove(self):
        candidate = build_candidate(("k(a) k(b) no(k(c)) no(k(d))", "a b c d"))
        self.assertFalse(candidate.proven())

        candidate = build_candidate(("k(a) k(b) no(k(c)) no(k(d))", "a b no(c) no(d)"))
        self.assertTrue(candidate.proven())

        candidate = build_candidate(
            ("k(a) k(b) no(k(no1(c))) no(k(not1(d)))", "a b no1(c) no(not1(d))")
        )
        self.assertFalse(candidate.proven())

        candidate = build_candidate(
            ("k(a) k(b) no(k(no1(c))) no(k(not1(d)))", "a b no(no1(c)) no(not1(d))")
        )
        self.assertTrue(candidate.proven())
