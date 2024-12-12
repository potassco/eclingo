# after removing InternalStateControl this does not work
import unittest

import clingo
from clingo import Number

import eclingo.internal_states.internal_control as internal_control
from eclingo import config as _config
from eclingo import grounder as _grounder
from eclingo.internal_states.internal_control import ShowStatement

# python -m unittest tests.test_grounder.Test.


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
        config = _config.AppConfig()
        config.eclingo_semantics = "c19-1"
        self.grounder = _grounder.Grounder(
            clingo.Control(message_limit=0),
            config=config,
        )

    def ground_program(self, program, parameters=None, arguments=None):
        if parameters is None and arguments is None:
            self.grounder.add_program(program)
            self.grounder.ground()
        else:
            self.grounder.add_program(program, parameters)
            self.grounder.ground([("base", arguments)])
        ground_program = self.grounder.control.ground_program
        return ground_program

    def assertEqualPrograms(self, ground_program, expected):
        expected = map(lambda x: x.lstrip().rstrip(), expected)
        ground_program = ground_program.pretty_str()
        ground_program = sorted(map(str, list(ground_program.split("\n"))))
        self.assertEqual(ground_program, sorted(expected))


class Test(TestCase):
    def test_epistemic_atom0(self):
        self.assertEqualPrograms(self.ground_program("{a}."), ["{u(a)}."])

    def test_epistemic_atom(self):
        self.assertEqualPrograms(
            self.ground_program("{a}. b :- &k{a}."),
            ["u(b) :- k(u(a)).", "{k(u(a))} :- u(a).", "{u(a)}."],
        )

    def test_epistemic_atom_with_strong_negation01(self):
        self.assertEqualPrograms(
            self.ground_program("{-a}. b :- &k{-a}."),
            ["u(b) :- k(u(-a)).", "{k(u(-a))} :- u(-a).", "{u(-a)}."],
        )

    def test_epistemic_atom_with_strong_negation02(self):
        self.assertEqualPrograms(
            self.ground_program("{a}. b :- &k{- -a}."),
            ["u(b) :- k(u(a)).", "{k(u(a))} :- u(a).", "{u(a)}."],
        )

    def test_epistemic_atom_with_default_negation01(self):
        self.assertEqualPrograms(
            self.ground_program("{a}. b :- &k{ not a}."),
            [
                "not1(u(a)) :- not u(a).",
                "u(b) :- k(not1(u(a))).",
                "{k(not1(u(a)))} :- not1(u(a)).",
                "{u(a)}.",
            ],
        )

    def test_epistemic_atom_with_default_negation02(self):
        self.assertEqualPrograms(
            self.ground_program("b :- &k{ not a}."),
            ["__x1.", "not1(u(a)).", "u(b) :- k(not1(u(a))).", "{k(not1(u(a)))}."],
        )

    def test_epistemic_atom_with_default_negation03(self):
        self.assertEqualPrograms(
            self.ground_program("{a}. b :- &k{ not not a}."),
            [
                "__x2 :- not u(a).",
                "not2(u(a)) :- not __x2.",
                "u(b) :- k(not2(u(a))).",
                "{k(not2(u(a)))} :- not2(u(a)).",
                "{u(a)}.",
            ],
        )

    def test_epistemic_atom_with_both_negations01(self):
        self.assertEqualPrograms(
            self.ground_program("{-a}. b :- &k{ not -a}."),
            [
                "not1(u(-a)) :- not u(-a).",
                "u(b) :- k(not1(u(-a))).",
                "{k(not1(u(-a)))} :- not1(u(-a)).",
                "{u(-a)}.",
            ],
        )

    def test_epistemic_atom_with_both_negations01b(self):
        self.assertEqualPrograms(
            self.ground_program("b :- &k{ not -a}."),
            ["__x1.", "not1(u(-a)).", "u(b) :- k(not1(u(-a))).", "{k(not1(u(-a)))}."],
        )

    def test_epistemic_atom_with_both_negations02(self):
        self.assertEqualPrograms(
            self.ground_program("{-a}. b:- &k{ not not -a}."),
            [
                "__x2 :- not u(-a).",
                "not2(u(-a)) :- not __x2.",
                "u(b) :- k(not2(u(-a))).",
                "{k(not2(u(-a)))} :- not2(u(-a)).",
                "{u(-a)}.",
            ],
        )

    def test_epistemic_with_variables01(self):
        self.assertEqualPrograms(
            self.ground_program("{a(1..2)}. b :- &k{a(V0)}."),
            [
                "u(b) :- k(u(a(1))).",
                "u(b) :- k(u(a(2))).",
                "{k(u(a(1)))} :- u(a(1)).",
                "{k(u(a(2)))} :- u(a(2)).",
                "{u(a(1))}.",
                "{u(a(2))}.",
            ],
        )

    def test_epistemic_with_variables02(self):
        self.assertEqualPrograms(
            self.ground_program("{-a(1..2)}. b :- &k{-a(V0)}."),
            [
                "u(b) :- k(u(-a(1))).",
                "u(b) :- k(u(-a(2))).",
                "{k(u(-a(1)))} :- u(-a(1)).",
                "{k(u(-a(2)))} :- u(-a(2)).",
                "{u(-a(1))}.",
                "{u(-a(2))}.",
            ],
        )

    def test_epistemic_with_variables03(self):
        self.assertEqualPrograms(
            self.ground_program("{a(1)}. b :- &k{- -a(V0)}."),
            ["u(b) :- k(u(a(1))).", "{k(u(a(1)))} :- u(a(1)).", "{u(a(1))}."],
        )

    def test_epistemic_with_variables04(self):
        self.assertEqualPrograms(
            self.ground_program("{a(1)}. dom(1). b :- &k{ not a(V0)}, dom(V0)."),
            [
                "__x1.",
                "not1(u(a(1))) :- not u(a(1)).",
                "u(b) :- k(not1(u(a(1)))).",
                "u(dom(1)).",
                "{k(not1(u(a(1))))} :- not1(u(a(1))).",
                "{u(a(1))}.",
            ],
        )

    def test_epistemic_with_variables05(self):
        self.assertEqualPrograms(
            self.ground_program("{a(1)}. dom(1). b :- &k{ not not a(V0)}, dom(V0)."),
            [
                "__x1.",
                "__x3 :- not u(a(1)).",
                "not2(u(a(1))) :- not __x3.",
                "u(b) :- k(not2(u(a(1)))).",
                "u(dom(1)).",
                "{k(not2(u(a(1))))} :- not2(u(a(1))).",
                "{u(a(1))}.",
            ],
        )

    def test_negated_epistemic_literals01(self):
        self.assertEqualPrograms(
            self.ground_program("{a(1..2)}. {b(1)}. c :- not &k{a(V0)}, &k{b(V0)}."),
            [
                "u(c) :- k(u(b(1))), not k(u(a(1))).",
                "{k(u(a(1)))} :- u(a(1)).",
                "{k(u(a(2)))} :- u(a(2)).",
                "{k(u(b(1)))} :- u(b(1)).",
                "{u(a(1))}.",
                "{u(a(2))}.",
                "{u(b(1))}.",
            ],
        )

    # def test_negated_epistemic_literals02(self):
    #     self.assertEqualPrograms(
    #         self.ground_program(":- not not &k{a(V0)}, &k{b(V0)}."),
    #         [
    #             ''
    #         ]
    #     )

    def test_parameters(self):
        self.assertEqualPrograms(
            self.ground_program("a(1..n).", ["n"], [Number(3)]),
            ["__x1.", "__x2.", "__x3.", "u(a(1)).", "u(a(2)).", "u(a(3))."],
        )

    def test_show01(self):
        self.assertEqualPrograms(
            self.ground_program("a. b. #show a/0."),
            ["__x1.", "__x2.", "__x3.", "show_statement(a).", "u(a).", "u(b)."],
        )

    def test_show02(self):
        self.assertEqualPrograms(
            self.ground_program("a. b. #show a/0. #show b/0."),
            [
                "__x1.",
                "__x2.",
                "__x3.",
                "__x4.",
                "show_statement(a).",
                "show_statement(b).",
                "u(a).",
                "u(b).",
            ],
        )

    def test_show03(self):
        self.assertEqualPrograms(
            self.ground_program("-a. b. #show -a/0."),
            ["__x1.", "__x2.", "u(-a).", "u(b)."],
        )
