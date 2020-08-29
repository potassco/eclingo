import unittest
import clingo
from eclingo.util.logger import silent_logger
import eclingo.parsing.transformers.transformer as _tf
from eclingo.parsing2 import ParseProgram
from eclingo.parsing.transformers.inspector import inspect_ast




class TestTheoryRemoveNegationsKRules(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.print = True
        self.control = clingo.Control(logger=silent_logger)
        self.output = ""
        
    def assert_ast(self, input, expected, aux_rules=None):
        
        sn_u_replacement = set()

        def fun(stm):
            if self.print:
                print("--- input -----------------")
                print(inspect_ast(stm))
                print("------------------")
            self.output += str(stm) + "\n"
        
        ParseProgram(input, fun)()

        if self.print:
            print("--- output ----------------------") 
            print(self.output)
        self.assertEqual(self.output.replace('\n', '').replace(' ', ''), expected.replace('\n', '').replace(' ', ''))


    def test_01(self):
        program = """
            :- &k{ a }.
        """
        expected = """
        #program base.
        #false :- k_u_a.
        """
        aux_rules = ""
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_02(self):
        program = """
            :- &k{ - a }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a.
        """
        aux_rules = "sn_u_a :- - u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_03(self):
        program = """
            :- &k{ - - a }.
        """
        expected = """
        #program base.
        #false :- k_u_a.
        """
        aux_rules = ""
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_04(self):
        program = """
            :- &k{ - - - a }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a.
        """
        aux_rules = "sn_u_a :- - u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_05(self):
        program = """
            :- &k{ not a }.
        """
        expected = """
        #program base.
        #false :- k_not_u_a.
        """
        aux_rules = "not_u_a :- not u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)

    def test_06(self):
        program = """
            :- &k{ not not a }.
        """
        expected = """
        #program base.
        #false :- k_not2_u_a.
        """
        aux_rules = "not2_u_a :- not not u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_07(self):
        program = """
            :- &k{ not -a }.
        """
        expected = """
        #program base.
        #false :- k_not_sn_u_a.
        """
        aux_rules = "not_sn_u_a :- not sn_u_a. sn_u_a :- -u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_08(self):
        program = """
            :- &k{ not not -a }.
        """
        expected = """
        #program base.
        #false :- k_not2_sn_u_a.
        """
        aux_rules = "not2_sn_u_a :- not not sn_u_a. sn_u_a :- -u_a."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_09(self):
        program = """
            :- &k{ a(2) }.
        """
        expected = """
        #program base.
        #false :- k_u_a(2).
        """
        aux_rules = ""
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_10(self):
        program = """
            :- &k{ a(X) }.
        """
        expected = """
        #program base.
        #false :- k_u_a(X).
        """
        aux_rules = ""
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)

    def test_11(self):
        program = """
            :- &k{ -a(2) }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a(2).
        """
        aux_rules = "sn_u_a(V0) :- -u_a(V0)."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_12(self):
        program = """
            :- &k{ -a(X) }.
        """
        expected = """
        #program base.
        #false :- k_sn_u_a(X).
        """
        aux_rules = "sn_u_a(V0) :- -u_a(V0)."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_13(self):
        program = """
            :- &k{ not a(X) }, b(X), not c(X).
        """
        expected = """
        #program base.
        #false :- k_not_u_a(X); u_b(X); not u_c(X).
        """
        aux_rules = "not_u_a(X) :- u_b(X); not u_c(X); not u_a(X)."
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_14(self):
        program = """
            :- &k{ not a(X) }, b(X), not c(X), &k{ -d(X) }.
        """
        expected = """
        #program base.
        #false :- k_not_u_a(X); u_b(X); not u_c(X); k_sn_u_d(X).
        """
        aux_rules = """
            not_u_a(X) :- u_b(X); not u_c(X); k_sn_u_d(X); not u_a(X).
            sn_u_d(V0) :- -u_d(V0).
        """
        expected = expected + aux_rules
        self.assert_ast(program, expected, aux_rules)


    def test_15(self):
        program = """
            a.
        """
        expected = """
        #programbase.
        u_a.
        """
        expected = expected
        self.assert_ast(program, expected)