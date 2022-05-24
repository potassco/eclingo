import unittest
from pprint import pprint

from clingo import Number

from eclingo import grounder as _grounder
from eclingo import config as _config
from eclingo import internal_states as _internal_states
from eclingo.internal_states import ShowSignature, ShowStatement
from eclingo.util import clingoext as _clingoext


def flatten(lst):
    result = []
    for lst2 in lst:
        if isinstance(lst2, list):
            for e in lst2:
                result.append(e)
        else:
            result.append(lst2)
    return result





class TestCase(unittest.TestCase):

    def setUp(self):
        self.print = False
        config   = _config.AppConfig()
        config.eclingo_semantics = "c19-1"
        self.grounder = _grounder.Grounder(_internal_states.InternalStateControl(control=_clingoext.Control(message_limit=0)), config=config)
        self.clingo_control_test = _clingoext.Control(message_limit=0)
        
    def ground_program(self, program, parameters=None, arguments=None):
        if parameters is None and arguments is None:
            self.grounder.add_program(program)
            self.grounder.ground()
        else:
            self.grounder.add_program(program, parameters)
            self.grounder.ground([("base", arguments)])
        ground_program = self.grounder.control.ground_program
        if self.print:
            print("\n--- non-ground program")
            pprint(self.grounder.control.parsed_program)
            print("\n--- program ---")
            pprint(ground_program.objects)
        return ground_program

    def assertEqualPrograms(self, ground_program, expected):
        expected = map(lambda x: x.lstrip().rstrip(), expected)
        ground_program = ground_program.pretty()
        ground_program = sorted(map(str, ground_program.as_list()))
        self.assertEqual(ground_program, sorted(expected))





class Test(TestCase):

    def test_epistemic_atom0(self):
        self.assertEqualPrograms(self.ground_program("{a}."), ["{u_a}."])

    def test_epistemic_atom(self):
        self.assertEqualPrograms(self.ground_program("{a}. b :- &k{a}."), ["{u_a}.", "u_b :- k_u_a.", "{k_u_a} :- u_a."])

    def test_epistemic_atom_with_strong_negation01(self):
        self.assertEqualPrograms(self.ground_program("{-a}. b :- &k{-a}."), ["{-u_a}.", "u_b :- k_sn_u_a.", "sn_u_a :- -u_a.", "{k_sn_u_a} :- sn_u_a."])
    def test_epistemic_atom_with_strong_negation02(self):
        self.assertEqualPrograms(self.ground_program("{a}. b :- &k{- -a}."), ["{u_a}.", "u_b :- k_u_a.", "{k_u_a} :- u_a."])

    def test_epistemic_atom_with_default_negation01(self):
        self.assertEqualPrograms(self.ground_program("{a}. b :- &k{ not a}."), [
            "{u_a}.",
            "u_b :- k_not_u_a.",
            "not_u_a :- not u_a.",
            "{k_not_u_a} :- not_u_a."])
    def test_epistemic_atom_with_default_negation02(self):
        self.assertEqualPrograms(self.ground_program("b :- &k{ not a}."), [
            "u_b :- k_not_u_a.",
            "not_u_a.",
            "{k_not_u_a}."])
    def test_epistemic_atom_with_default_negation03(self):
        self.assertEqualPrograms(self.ground_program("{a}. b :- &k{ not not a}."), [
            "{u_a}.",
            "u_b :- k_not2_u_a.",
            "not2_u_a :- not x_2.",
            "x_2 :- not u_a.",
            "{k_not2_u_a} :- not2_u_a."])

    def test_epistemic_atom_with_both_negations01(self):
        self.assertEqualPrograms(self.ground_program("{-a}. b :- &k{ not -a}."), [
            "{-u_a}.",
            "u_b :- k_not_sn_u_a.",
            "not_sn_u_a :- not sn_u_a.",
            "{k_not_sn_u_a} :- not_sn_u_a.",
            "sn_u_a :- -u_a."])
    def test_epistemic_atom_with_both_negations01b(self):
        self.assertEqualPrograms(self.ground_program("b :- &k{ not -a}."), [
            "u_b :- k_not_sn_u_a.",
            "not_sn_u_a.",
            "{k_not_sn_u_a}."])
    def test_epistemic_atom_with_both_negations02(self):
        self.assertEqualPrograms(self.ground_program("{-a}. b:- &k{ not not -a}."), [
            "{-u_a}.",
            "u_b :- k_not2_sn_u_a.",
            "not2_sn_u_a :- not x_3.",
            "x_3 :- not sn_u_a.",
            "{k_not2_sn_u_a} :- not2_sn_u_a.",
            "sn_u_a :- -u_a."])

    def test_epistemic_with_variables01(self):
        self.assertEqualPrograms(self.ground_program("{a(1..2)}. b :- &k{a(V0)}."), [
            "{u_a(1)}.",
            "{u_a(2)}.",
            "u_b :- k_u_a(1).",
            "u_b :- k_u_a(2).",
            "{k_u_a(1)} :- u_a(1).",
            "{k_u_a(2)} :- u_a(2)."])
    def test_epistemic_with_variables02(self):
        self.assertEqualPrograms(self.ground_program("{-a(1..2)}. b :- &k{-a(V0)}."), [
            "{-u_a(1)}.",
            "{-u_a(2)}.",
            "u_b :- k_sn_u_a(1).",
            "u_b :- k_sn_u_a(2).",
            "sn_u_a(1) :- -u_a(1).",
            "sn_u_a(2) :- -u_a(2).",
            "{k_sn_u_a(1)} :- sn_u_a(1).",
            "{k_sn_u_a(2)} :- sn_u_a(2)."])
    def test_epistemic_with_variables03(self):
        self.assertEqualPrograms(self.ground_program("{a(1)}. b :- &k{- -a(V0)}."), [
            "{u_a(1)}.",
            "u_b :- k_u_a(1).",
            "{k_u_a(1)} :- u_a(1)."])
    def test_epistemic_with_variables04(self):
        self.assertEqualPrograms(self.ground_program("{a(1)}. dom(1). b :- &k{ not a(V0)}, dom(V0)."), [
            "u_dom(1).",
            "{u_a(1)}.",
            "u_b :- k_not_u_a(1).",
            "not_u_a(1) :- not u_a(1).",
            "{k_not_u_a(1)} :- not_u_a(1)."])
    def test_epistemic_with_variables05(self):
        self.assertEqualPrograms(self.ground_program("{a(1)}. dom(1). b :- &k{ not not a(V0)}, dom(V0)."), [
            "u_dom(1).",
            "{u_a(1)}.",
            "u_b :- k_not2_u_a(1).",
            "not2_u_a(1) :- not x_3.",
            "x_3 :- not u_a(1).",
            "{k_not2_u_a(1)} :- not2_u_a(1)."])

    def test_negated_epistemic_literals01(self):
        self.assertEqualPrograms(self.ground_program("{a(1..2)}. {b(1)}. c :- not &k{a(V0)}, &k{b(V0)}."), [
            "{u_a(1)}.",
            "{u_a(2)}.",
            "{u_b(1)}.",
            "u_c :- k_u_b(1), not k_u_a(1).",
            "{k_u_a(1)} :- u_a(1).",
            "{k_u_a(2)} :- u_a(2).",
            "{k_u_b(1)} :- u_b(1)."])
    # def test_negated_epistemic_literals02(self):
    #     self.assertEqualPrograms(self.ground_program(":- not not &k{a(V0)}, &k{b(V0)}."), """
    #         :- not not k_u_a(V0), k_u_b(V0).
    #         {k_u_a(V0)} :- u_a(V0).
    #         {k_u_b(V0)} :- u_b(V0).
    #         """)

    def test_parameters(self):
        self.assertEqualPrograms(self.ground_program("a(1..n).", ["n"], [Number(3)]), ["u_a(1).", "u_a(2).", "u_a(3)."])

    def test_show01(self):
        self.assertEqualPrograms(self.ground_program("a. b. #show a/0."), ["u_a.", "u_b."])
        show_signature = ShowSignature({ShowStatement(name='a', arity=0, poistive=True)})
        self.assertEqual(self.grounder.control.show_signature, show_signature)


    def test_show02(self):
        self.assertEqualPrograms(self.ground_program("a. b. #show a/0. #show b/0."), ["u_a.", "u_b."])
        show_signature = ShowSignature({
            ShowStatement(name='a', arity=0, poistive=True),
            ShowStatement(name='b', arity=0, poistive=True)
        })
        self.assertEqual(self.grounder.control.show_signature, show_signature)

    def test_show03(self):
        self.assertEqualPrograms(self.ground_program("-a. b. #show -a/0."), ["-u_a.", "u_b."])
        show_signature = ShowSignature({ShowStatement(name='a', arity=0, poistive=False)})
        self.assertEqual(self.grounder.control.show_signature, show_signature)
