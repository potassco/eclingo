from eclingo import internal_states
from eclingo.internal_states import ShowStatement
import unittest
import clingo
from eclingo.util.astutil import ast_repr as _ast_repr
from eclingo.parsing import parse_program as _parse_program


def parse_formula(stm):
    ret = []
    prg = clingo.Control(message_limit=0)
    clingo.parse_program(stm + ".", ret.append)
    return ret[-1]

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
    _parse_program(stm, ret.append, parameters, name)
    return flatten(ret)

def clingo_parse_program(stm):
    ret = []
    clingo.parse_program(stm, ret.append)
    return ret

class TestCase(unittest.TestCase):

    def setUp(self):
        self.print = False

    def assertEqualFormula(self, formula, expected):
        expected_formula = parse_formula(expected)
        if self.print:
            print("--- formula ---")
            print(_ast_repr(formula))
            print("--- expected formula ---")
            print(_ast_repr(expected_formula))
        self.assertEqual(formula, expected_formula)

    def assert_equal_program(self, program, expected):
        expected_program = clingo_parse_program(expected)
        if self.print:
            print("--- program ---")
            print(_ast_repr(program))
            print("--- expected program ---")
            print(_ast_repr(expected_program))
        self.assertEqual(sorted(program), sorted(expected_program))

    def assert_equal_program_with_show(self, program, expected, expected_show):
        program_without_show = []
        show_statements = []
        for statement in program:
            if isinstance(statement, ShowStatement):
                show_statements.append(statement)
            else:
                program_without_show.append(statement)
        expected_program = clingo_parse_program(expected)
        if self.print:
            print("--- program ---")
            print(_ast_repr(program_without_show))
            print("--- expected program ---")
            print(_ast_repr(expected_program))
        self.assertEqual(sorted(program_without_show), sorted(expected_program))
        self.assertEqual(sorted(show_statements), sorted(expected_show))





class Test(TestCase):

    def test_epistemic_atom(self):
        self.assert_equal_program(parse_program(":- &k{a}."), ":- k_u_a. {k_u_a} :- u_a.")

    def test_epistemic_atom_with_strong_negation(self):
        self.assert_equal_program(parse_program(":- &k{-a}."), ":- k_sn_u_a. sn_u_a :- -u_a. {k_sn_u_a} :- sn_u_a.")
        self.assert_equal_program(parse_program(":- &k{- -a}."), ":- k_u_a. {k_u_a} :- u_a.")

    def test_epistemic_atom_with_default_negation(self):
        self.assert_equal_program(parse_program(":- &k{ not a}."), ":- k_not_u_a. not_u_a :- not u_a. {k_not_u_a} :- not_u_a.")
        self.assert_equal_program(parse_program("b :- &k{ not a}."), "u_b :- k_not_u_a. not_u_a :- not u_a. {k_not_u_a} :- not_u_a.")
        self.assert_equal_program(parse_program(":- &k{ not not a}."), ":- k_not2_u_a. not2_u_a :- not not u_a. {k_not2_u_a} :- not2_u_a.")

    def test_epistemic_atom_with_both_negations(self):
        self.assert_equal_program(parse_program(":- &k{ not -a}."), ":- k_not_sn_u_a. not_sn_u_a :- not sn_u_a. {k_not_sn_u_a} :- not_sn_u_a. sn_u_a :- -u_a.")
        self.assert_equal_program(parse_program(":- &k{ not not -a}."), ":- k_not2_sn_u_a. not2_sn_u_a :- not not sn_u_a.  {k_not2_sn_u_a} :- not2_sn_u_a. sn_u_a :- -u_a.")

    def test_epistemic_with_variables(self):
        self.assert_equal_program(parse_program(":- &k{a(V0)}."), ":- k_u_a(V0). {k_u_a(V0)} :- u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{-a(V0)}."), ":- k_sn_u_a(V0). sn_u_a(V0) :- -u_a(V0). {k_sn_u_a(V0)} :- sn_u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{- -a(V0)}."), ":- k_u_a(V0). {k_u_a(V0)} :- u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{ not a(V0)}."), ":- k_not_u_a(V0). not_u_a(V0) :- not u_a(V0). {k_not_u_a(V0)} :- not_u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{ not not a(V0)}."), ":- k_not2_u_a(V0). not2_u_a(V0) :- not not u_a(V0). {k_not2_u_a(V0)} :- not2_u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{ not -a(V0)}."), ":- k_not_sn_u_a(V0). not_sn_u_a(V0) :- not sn_u_a(V0). {k_not_sn_u_a(V0)} :- not_sn_u_a(V0). sn_u_a(V0) :- -u_a(V0).")
        self.assert_equal_program(parse_program(":- &k{ not not -a(V0)}."), ":- k_not2_sn_u_a(V0). not2_sn_u_a(V0) :- not not sn_u_a(V0).  {k_not2_sn_u_a(V0)} :- not2_sn_u_a(V0). sn_u_a(V0) :- -u_a(V0).")

    def test_epistemic_with_variables_safety01(self):
        self.assert_equal_program(parse_program(":- &k{a(V0)}, not b(V0)."), """
            :- k_u_a(V0), not u_b(V0).
            { k_u_a(V0) :  } :- u_a(V0).
            """)

    def test_epistemic_with_variables_safety02(self):
        self.assert_equal_program(parse_program(":- a(V0), &k{not b(V0)}."), """
            :- u_a(V0), k_not_u_b(V0).
            not_u_b(V0) :- u_a(V0), not u_b(V0).
            { k_not_u_b(V0) :  } :- not_u_b(V0).
            """)

    def test_epistemic_with_variables_safety03(self):
        self.assert_equal_program(parse_program(":- &k{a(V0)}, &k{not b(V0)}."), """
            :- k_u_a(V0), k_not_u_b(V0).
            not_u_b(V0) :- k_u_a(V0), not u_b(V0).
            { k_not_u_b(V0) :  } :- not_u_b(V0).
            { k_u_a(V0) :  } :- u_a(V0).
            { k_u_a(V0) :  } :- u_a(V0).
            """)
    # Note that the last two rules appear repeated. The second copy apears when processing the rules
    # not_u_b(V0) :- &k{u_a(V0)}, not u_b(V0).
    # An improvement would removing those unecessary rules

    def test_epistemic_with_variables_safety04(self):
            self.assert_equal_program(parse_program('b :- not not &k{a(X)}.'), """
            u_b :- not not k_u_a(X).
            { k_u_a(X) : } :- u_a(X).
            """)

    def test_negated_epistemic_literals(self):
        self.assert_equal_program(parse_program(":- not &k{a(V0)}, &k{b(V0)}."), """
            :- not k_u_a(V0), k_u_b(V0).
            {k_u_a(V0)} :- u_a(V0).
            {k_u_b(V0)} :- u_b(V0).
            """)
        self.assert_equal_program(parse_program(":- not not &k{a(V0)}, &k{b(V0)}."), """
            :- not not k_u_a(V0), k_u_b(V0).
            {k_u_a(V0)} :- u_a(V0).
            {k_u_b(V0)} :- u_b(V0).
            """)

    def test_weighted_rules(self):
        self.assert_equal_program(parse_program(":-{a} = 0."), ":-{u_a} = 0.")

    def test_parameters01(self):
        self.assert_equal_program(parse_program("a(1..n).", ["n"], "parametrized" ), "#program parametrized(n). u_a(1..n).")

    def test_parameters02(self):
        self.assert_equal_program(parse_program("a(1..n).", ["n"], "base" ), "#program base(n). u_a(1..n).")

    
