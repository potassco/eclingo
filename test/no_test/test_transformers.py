import unittest
import clingo
from eclingo.util.logger import silent_logger
import eclingo.parsing.transformers.transformer as _tf
from eclingo.parsing.transformers import parse_epistemic_literals
from eclingo.parsing.transformers import  strong_negation_auxiliary_rule_replacement
from eclingo.parsing.transformers.inspector import inspect_ast




class TestTheoryRemoveNegationsKRules(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.print = True
        self.control = clingo.Control(logger=silent_logger)
        self.intermediate = ""
        self.output = ""
        self.aux_rules = []
        
    def assert_ast(self, input, expected, aux_rules=None):
        
        sn_u_replacement = set()

        def fun(stm):
            if self.print:
                print("--- input -----------------")
                print(inspect_ast(stm))
                print("------------------")
            stm, aux_rules, replacement = parse_epistemic_literals(stm)
            sn_u_replacement.update(replacement)
            self.output += str(stm) + "\n"
            self.aux_rules.extend(aux_rules)
        
        clingo.parse_program(input, fun)
        
        rules = list(strong_negation_auxiliary_rule_replacement(sn_u_replacement))
        self.aux_rules.extend(rules)
        self.aux_rules.sort()

        if self.print:
            print("--- output ----------------------") 
            print(self.output)
            print("--- aux_rules ----------------------") 
            print(self.aux_rules)
        self.assertEqual(self.output.replace('\n', '').replace(' ', ''), expected.replace('\n', '').replace(' ', ''))
        
        if aux_rules is not None:
            self.assertEqual(str(self.aux_rules).replace('\n', '').replace(' ', ''), aux_rules.replace('\n', '').replace(' ', ''))


    def test_01(self):
        program = """
            :- &k{ a }.
        """
        expected = """[
        #program base.
        #false :- k_u_a. ,
        {k_u_a:} :- u_a.
        ]"""
        aux_rules = "[]"
        self.assert_ast(program, expected, aux_rules)


    def test_02(self):
        program = """
            :- &k{ - a }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a.
        """
        aux_rules = "[sn_u_a :- - u_a.]"
        self.assert_ast(program, expected, aux_rules)


    def test_03(self):
        program = """
            :- &k{ - - a }.
        """
        expected = """
        #program base.
        #false :- k_u_a.
        """
        aux_rules = "[]"
        self.assert_ast(program, expected, aux_rules)


    def test_04(self):
        program = """
            :- &k{ - - - a }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a.
        """
        aux_rules = "[sn_u_a :- - u_a.]"
        self.assert_ast(program, expected, aux_rules)


    def test_05(self):
        program = """
            :- &k{ not a }.
        """
        expected = """
        #program base.
        #false :- k_not_u_a.
        """
        aux_rules = "[not_u_a :- not u_a.]"
        self.assert_ast(program, expected, aux_rules)

    def test_06(self):
        program = """
            :- &k{ not not a }.
        """
        expected = """
        #program base.
        #false :- k_not2_u_a.
        """
        aux_rules = "[not2_u_a :- not not u_a.]"
        self.assert_ast(program, expected, aux_rules)


    def test_07(self):
        program = """
            :- &k{ not -a }.
        """
        expected = """
        #program base.
        #false :- k_not_sn_u_a.
        """
        aux_rules = "[sn_u_a :- -u_a. , not_sn_u_a :- not sn_u_a.]"
        self.assert_ast(program, expected, aux_rules)


    def test_08(self):
        program = """
            :- &k{ not not -a }.
        """
        expected = """
        #program base.
        #false :- k_not2_sn_u_a.
        """
        aux_rules = "[sn_u_a :- -u_a. , not2_sn_u_a :- not not sn_u_a.]"
        self.assert_ast(program, expected, aux_rules)


    def test_09(self):
        program = """
            :- &k{ a(2) }.
        """
        expected = """
        #program base.
        #false :- k_u_a(2).
        """
        aux_rules = "[]"
        self.assert_ast(program, expected, aux_rules)


    def test_10(self):
        program = """
            :- &k{ a(X) }.
        """
        expected = """
        #program base.
        #false :- k_u_a(X).
        """
        aux_rules = "[]"
        self.assert_ast(program, expected, aux_rules)

    def test_11(self):
        program = """
            :- &k{ -a(2) }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a(2).
        """
        aux_rules = "[sn_u_a(V0) :- -u_a(V0).]"
        self.assert_ast(program, expected, aux_rules)


    def test_12(self):
        program = """
            :- &k{ -a(X) }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a(X).
        """
        aux_rules = "[sn_u_a(V0) :- -u_a(V0).]"
        self.assert_ast(program, expected, aux_rules)


    def test_13(self):
        program = """
            :- &k{ not a(X) }, b(X), not c(X).
        """
        expected = """
        #program base.
        #false :- k_not_u_a(X); u_b(X); not u_c(X).
        """
        aux_rules = "[not_u_a(X) :- u_b(X); not u_c(X); not u_a(X).]"
        self.assert_ast(program, expected, aux_rules)


    def test_14(self):
        program = """
            :- &k{ not a(X) }, b(X), not c(X), &k{ -d(X) }.
        """
        expected = """
        #program base.
        #false :- k_not_u_a(X); u_b(X); not u_c(X); k_sn_u_d(X).
        """
        aux_rules = """[
            sn_u_d(V0) :- -u_d(V0). ,
            not_u_a(X) :- u_b(X); not u_c(X); k_sn_u_d(X); not u_a(X).
        ]"""
        self.assert_ast(program, expected, aux_rules)