from clingo import ast
from clingox.testing.ast import ASTTestCase

from eclingo.config import AppConfig
from eclingo.parsing import parser
from eclingo.parsing.transformers import function_transformer

# python -m unittest tests.test_reification.Test.test_epistemic_atom


def flatten(lst):
    result = []
    for lst2 in lst:
        if isinstance(lst2, list):
            for e in lst2:
                result.append(e)
        else:
            result.append(lst2)

    return result


def parse_program(stm, parameters=[], name="base"):
    ret = []
    parser.parse_program(
        stm,
        ret.append,
        parameters,
        name,
        config=AppConfig(semantics="c19-1", verbose=0),
    )
    return flatten(ret)


def clingo_parse_program(stm):
    ret = []
    ast.parse_string(stm, ret.append)
    ret = [rule for rule in ret]
    return ret


class TestCase(ASTTestCase):
    def setUp(self):
        self.print = False

    def assert_equal_program(self, program, expected):
        expected_program = clingo_parse_program(expected)
        expected_program = [
            function_transformer.rule_to_symbolic_term_adapter(stm)
            for stm in expected_program
        ]

        program = [
            function_transformer.rule_to_symbolic_term_adapter(stm) for stm in program
        ]

        sorted_program = sorted(program)
        expected_program.sort()

        if len(sorted_program) != len(expected_program):
            self.fail(
                f"Lists differ (different lenghts {len(sorted_program)} and {len(expected_program)}"
            )
        for e1, e2 in zip(sorted_program, expected_program):
            self.assertEqual(e1, e2)
        self.assertListEqual(sorted_program, expected_program)


class Test(TestCase):
    def test_non_epistemic_rules(self):
        self.assert_equal_program(
            parse_program("a :- b, c, not d, not not e."),
            "u(a) :- u(b), u(c), not u(d), not not u(e).",
        )

        self.assert_equal_program(
            parse_program("a :- b."),
            "u(a) :- u(b).",
        )

        self.assert_equal_program(
            parse_program("-a :- b, -c, not -d, not not -e."),
            "u(-a) :- u(b), u(-c), not u(-d), not not u(-e).",
        )

    def test_epistemic_atom(self):
        self.assert_equal_program(
            parse_program(":- &k{a}."), ":- k(u(a)). {k(u(a))} :- u(a)."
        )

    def test_epistemic_atom_with_strong_negation(self):
        self.assert_equal_program(
            parse_program(":- &k{-a}."),
            ":- k(u(-a)). {k(u(-a))} :- u(-a).",
        )

        self.assert_equal_program(
            parse_program(":- &k{- -a}."), ":- k(u(a)). {k(u(a))} :- u(a)."
        )

    def test_epistemic_atom_with_default_negation(self):
        self.assert_equal_program(
            parse_program(":- &k{ not a}."),
            ":- k(not1(u(a))). not1(u(a)) :- not u(a). {k(not1(u(a)))} :- not1(u(a)).",
        )

        self.assert_equal_program(
            parse_program("b :- &k{ not a}."),
            "u(b) :- k(not1(u(a))). not1(u(a)) :- not u(a). {k(not1(u(a)))} :- not1(u(a)).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not not a}."),
            ":- k(not2(u(a))). not2(u(a)) :- not not u(a). {k(not2(u(a)))} :- not2(u(a)).",
        )

    def test_epistemic_atom_with_both_negations(self):
        self.assert_equal_program(
            parse_program(":- &k{ not -a}."),
            ":- k(not1(u(-a))). not1(u(-a)) :- not u(-a). {k(not1(u(-a)))} :- not1(u(-a)).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not not -a}."),
            ":- k(not2(u(-a))). not2(u(-a)) :- not not u(-a).  {k(not2(u(-a)))} :- not2(u(-a)).",
        )

    def test_epistemic_with_variables(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}."), ":- k(u(a(V0))). {k(u(a(V0)))} :- u(a(V0))."
        )
        self.assert_equal_program(
            parse_program(":- &k{- -a(V0)}."),
            ":- k(u(a(V0))). {k(u(a(V0)))} :- u(a(V0)).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not a(V0)}."),
            ":- k(not1(u(a(V0)))). not1(u(a(V0))) :- not u(a(V0)). {k(not1(u(a(V0))))} :- not1(u(a(V0))).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not not a(V0)}."),
            ":- k(not2(u(a(V0)))). not2(u(a(V0))) :- not not u(a(V0)). {k(not2(u(a(V0))))} :- not2(u(a(V0))).",
        )

        self.assert_equal_program(
            parse_program(":- &k{-a(V0)}."),
            ":- k(u(-a(V0))). {k(u(-a(V0)))} :- u(-a(V0)).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not -a(V0)}."),
            ":- k(not1(u(-a(V0)))). not1(u(-a(V0))) :- not u(-a(V0)). {k(not1(u(-a(V0))))} :- not1(u(-a(V0))).",
        )

        self.assert_equal_program(
            parse_program(":- &k{ not not -a(V0)}."),
            ":- k(not2(u(-a(V0)))). not2(u(-a(V0))) :- not not u(-a(V0)). {k(not2(u(-a(V0))))} :- not2(u(-a(V0))).",
        )

    def test_epistemic_with_variables_safety01(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}, not b(V0)."),
            """
            :- k(u(a(V0))), not u(b(V0)).
            { k(u(a(V0))) :  } :- u(a(V0)).
            """,
        )

    def test_epistemic_with_variables_safety02(self):
        self.assert_equal_program(
            parse_program(":- a(V0), &k{not b(V0)}."),
            """
            :- u(a(V0)), k(not1(u(b(V0)))).
            not1(u(b(V0))) :- u(a(V0)), not u(b(V0)).
            { k(not1(u(b(V0)))) :  } :- not1(u(b(V0))).
            """,
        )

    def test_epistemic_with_variables_safety03(self):
        self.assert_equal_program(
            parse_program(":- &k{a(V0)}, &k{not b(V0)}."),
            """
            :- k(u(a(V0))), k(not1(u(b(V0)))).
            not1(u(b(V0))) :- k(u(a(V0))), not u(b(V0)).
            { k(not1(u(b(V0)))) :  } :- not1(u(b(V0))).
            { k(u(a(V0))) :  } :- u(a(V0)).
            { k(u(a(V0))) :  } :- u(a(V0)).
            """,
        )

    """
    # # Note that the last two rules appear repeated. The second copy apears when processing the rules
    # # not_u_b(V0) :- &k{u_a(V0)}, not u_b(V0).
    # # An improvement would removing those unecessary rules
    """

    def test_epistemic_with_variables_safety04(self):
        self.assert_equal_program(
            parse_program("b :- not not &k{a(X)}."),
            """
            u(b) :- not not k(u(a(X))).
            { k(u(a(X))) : } :- u(a(X)).
            """,
        )

    def test_negated_epistemic_literals(self):
        self.assert_equal_program(
            parse_program(":- not &k{a(V0)}, &k{b(V0)}."),
            """
            :- not k(u(a(V0))), k(u(b(V0))).
            {k(u(a(V0)))} :- u(a(V0)).
            {k(u(b(V0)))} :- u(b(V0)).
            """,
        )
        self.assert_equal_program(
            parse_program(":- not not &k{a(V0)}, &k{b(V0)}."),
            """
            :- not not k(u(a(V0))), k(u(b(V0))).
            {k(u(a(V0)))} :- u(a(V0)).
            {k(u(b(V0)))} :- u(b(V0)).
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
