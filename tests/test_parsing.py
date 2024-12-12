import unittest

from clingo import ast

from eclingo.parsing import parser

# python -m unittest tests.test_parsing.Test.


def flatten(lst):
    result = []
    for lst2 in lst:
        if isinstance(lst2, list):
            for e in lst2:
                result.append(str(e))
        else:
            result.append(str(lst2))

    return result


def parse_program(stm, parameters=[], name="base"):
    ret = []
    parser.parse_program(stm, ret.append, parameters, name)
    return flatten(ret)


def clingo_parse_program(stm):
    ret = []
    ast.parse_string(stm, ret.append)
    ret = [str(rule) for rule in ret]
    return ret


class TestCase(unittest.TestCase):
    def setUp(self):
        self.print = False

    def assert_equal_program(self, program, expected):
        expected_program = clingo_parse_program(expected)
        self.assertCountEqual(sorted(program), sorted(expected_program))


class Test(TestCase):
    def test_epistemic_atom(self):
        self.assert_equal_program(
            parse_program(":- &k{a}."), ":- k(u(a)). {k(u(a))} :- u(a)."
        )

    def test_epistemic_atom_with_strong_negation(self):
        self.assert_equal_program(
            parse_program(":- &k{-a}."),
            ":- k(u(-a)). { k(u(-a)) } :- u(-a).",
        )
        self.assert_equal_program(
            parse_program(":- &k{- -a}."), ":- k(u(a)). { k(u(a)) } :- u(a)."
        )

    def test_epistemic_atom_with_default_negation(self):
        self.assert_equal_program(
            parse_program(":- &k{ not a}."),
            ":- k(not1(u(a))). not1(u(a)) :- not u(a). { k(not1(u(a))) } :- not1(u(a)).",
        )
        self.assert_equal_program(
            parse_program("b :- &k{ not a}."),
            "u(b) :- k(not1(u(a))). not1(u(a)) :- not u(a). { k(not1(u(a))) } :- not1(u(a)).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not not a}."),
            ":- k(not2(u(a))). not2(u(a)) :- not not u(a). { k(not2(u(a))) } :- not2(u(a)).",
        )

    def test_epistemic_atom_with_both_negations(self):
        self.assert_equal_program(
            parse_program(":- &k{ not -a}."),
            ":- k(not1(u(-a))). not1(u(-a)) :- not u(-a). { k(not1(u(-a))) } :- not1(u(-a)).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not not -a}."),
            ":- k(not2(u(-a))). not2(u(-a)) :- not not u(-a). { k(not2(u(-a))) } :- not2(u(-a)).",
        )

    def test_epistemic_with_variables(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}."),
            ":- k(u(a(V0))). { k(u(a(V0))) } :- u(a(V0)).",
        )
        self.assert_equal_program(
            parse_program(":- &k{-a(V0)}."),
            ":- k(u(-a(V0))). { k(u(-a(V0))) } :- u(-a(V0)).",
        )
        self.assert_equal_program(
            parse_program(":- &k{- -a(V0)}."),
            ":- k(u(a(V0))). { k(u(a(V0))) } :- u(a(V0)).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not a(V0)}."),
            ":- k(not1(u(a(V0)))). not1(u(a(V0))) :- not u(a(V0)). { k(not1(u(a(V0)))) } :- not1(u(a(V0))).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not not a(V0)}."),
            ":- k(not2(u(a(V0)))). not2(u(a(V0))) :- not not u(a(V0)). { k(not2(u(a(V0)))) } :- not2(u(a(V0))).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not -a(V0)}."),
            ":- k(not1(u(-a(V0)))). not1(u(-a(V0))) :- not u(-a(V0)). { k(not1(u(-a(V0)))) } :- not1(u(-a(V0))).",
        )
        self.assert_equal_program(
            parse_program(":- &k{ not not -a(V0)}."),
            ":- k(not2(u(-a(V0)))). not2(u(-a(V0))) :- not not u(-a(V0)).  { k(not2(u(-a(V0)))) } :- not2(u(-a(V0))).",
        )

    def test_epistemic_with_variables_safety01(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}, not b(V0)."),
            """
            :- k(u(a(V0))); not u(b(V0)).
            { k(u(a(V0))) } :- u(a(V0)).
            """,
        )

    def test_epistemic_with_variables_safety02(self):
        self.assert_equal_program(
            parse_program(":- a(V0), &k{not b(V0)}."),
            """
            :- u(a(V0)); k(not1(u(b(V0)))).
            not1(u(b(V0))) :- u(a(V0)); not u(b(V0)).
            { k(not1(u(b(V0)))) } :- not1(u(b(V0))).
            """,
        )

    def test_epistemic_with_variables_safety03(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}, &k{not b(V0)}."),
            """
            :- k(u(a(V0))); k(not1(u(b(V0)))).
            not1(u(b(V0))) :- k(u(a(V0))), not u(b(V0)).
            { k(not1(u(b(V0)))) :  } :- not1(u(b(V0))).
            { k(u(a(V0))) :  } :- u(a(V0)).
            { k(u(a(V0))) :  } :- u(a(V0)).
            """,
        )

    # # Note that the last two rules appear repeated. The second copy apears when processing the rules
    # # not_u_b(V0) :- &k{u_a(V0)}, not u_b(V0).
    # # An improvement would removing those unecessary rules

    def test_epistemic_with_variables_safety04(self):
        self.assert_equal_program(
            parse_program("b :- not not &k{a(X)}."),
            """
            u(b) :- not not k(u(a(X))).
            { k(u(a(X))) } :- u(a(X)).
            """,
        )

    def test_negated_epistemic_literals(self):
        self.assert_equal_program(
            parse_program(":- not &k{a(V0)}, &k{b(V0)}."),
            """
            :- not k(u(a(V0))); k(u(b(V0))).
            { k(u(a(V0))) } :- u(a(V0)).
            { k(u(b(V0))) } :- u(b(V0)).
            """,
        )
        self.assert_equal_program(
            parse_program(":- not not &k{a(V0)}, &k{b(V0)}."),
            """
             :- not not k(u(a(V0))); k(u(b(V0))).
            { k(u(a(V0))) } :- u(a(V0)).
            { k(u(b(V0))) } :- u(b(V0)).
            """,
        )

    def test_weighted_rules(self):
        self.assert_equal_program(parse_program(":-{a} = 0."), ":-{u(a)} = 0.")

    def test_parameters01(self):
        self.assert_equal_program(
            parse_program("a(1..n).", ["n"], "parametrized"),
            "#program parametrized(n). u(a(1..n)).",
        )

    def test_parameters02(self):
        self.assert_equal_program(
            parse_program("a(1..n).", ["n"], "base"), "#program base(n). u(a(1..n))."
        )

    def test_heuristic(self):
        self.assert_equal_program(
            parse_program("#heuristic a. [1,sign]", [], "base"),
            "#heuristic u(a). [1,sign]",
        )


class MandOldNegationTest(TestCase):
    def test_epistemic_atom(self):
        self.assert_equal_program(
            parse_program(":- &m{a}."),
            ":- not k(not1(u(a))). {k(not1(u(a)))} :- not1(u(a)). not1(u(a)) :- not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- &m{not a}."),
            ":- not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- &m{not not a}."),
            ":- not k(not1(u(a))). {k(not1(u(a)))} :- not1(u(a)). not1(u(a)) :- not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not &m{not a}."),
            ":- not not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not &m{not a}."),
            ":- not not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not &m{not not a}."),
            ":- not not k(not1(u(a))). {k(not1(u(a)))} :- not1(u(a)). not1(u(a)) :- not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not not &m{a}."),
            ":- not k(not1(u(a))). {k(not1(u(a)))} :- not1(u(a)). not1(u(a)) :- not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not not &m{not a}."),
            ":- not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not not &m{not not a}."),
            ":- not k(not1(u(a))). {k(not1(u(a)))} :- not1(u(a)). not1(u(a)) :- not u(a).",
        )

        self.assert_equal_program(
            parse_program(":- not &m{~ a}."),
            ":- not not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not &m{~ a}."),
            ":- not not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
        self.assert_equal_program(
            parse_program(":- not not &m{~ a}."),
            ":- not k(not2(u(a))). {k(not2(u(a)))} :- not2(u(a)). not2(u(a)) :- not not u(a).",
        )
