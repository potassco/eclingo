from parametrized import ParametrizedTestCase
from literals import * # pylint: disable=wildcard-import, unused-wildcard-import
import eclingo
from eclingo.util.logger import silent_logger

def append_candidates(obtained_candidates, candidate):
    pos = sorted(candidate[0])
    neg = sorted(candidate[1])
    candidate = (pos, neg)
    obtained_candidates.append(candidate)

class TestClingo(ParametrizedTestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.econtrol = eclingo.Control(control=self.control, config=self.param)
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
        obtained_wvs = [wv for wv in self.econtrol.solve()]
        print(str(obtained_wvs[0]))
        # self.assertEqual(wvs, obtained_wvs)

    def test_cycle_knot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not a }.
        """
        wvs = [([], [knota])]
        self.prepare(program)
        self.assertWV(wvs)

    # def test_pseudo_fact_K(self):
    #     program = """
    #     {a}.
    #     :- not a.
    #     b :- &k{ a }.
    #     """
    #     wvs = [([ka], [])]
    #     self.prepare(program)
    #     self.assertWV(wvs)