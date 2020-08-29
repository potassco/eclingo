import unittest
import clingo
from eclingo.util.logger import silent_logger
import eclingo.parsing.transformers.transformer as _tf
from eclingo.parsing.transformers.theory_parser_literals import theory_term_to_literal
from eclingo.parsing.transformers.parser_negations import make_strong_negations_auxiliar, make_default_negation_auxiliar
from eclingo.parsing.transformers.inspector import inspect_ast


class TransformerForTest(_tf.Transformer):

    def visit_TheoryAtom(self, atom, loc="body"):
        """
        TheoryAtom(location: Location, term: term, elements: TheoryAtomElement*)
        """
        result = atom
        if atom.term.name == "k" and not atom.term.arguments:
            result.elements = [theory_term_to_literal(e) for e in atom.elements]
        return result

TRANSFORMERFORTEST = TransformerForTest()

class TestTheoryRemoveNegations(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.print = True
        self.control = clingo.Control(logger=silent_logger)
        self.intermediate = ""
        self.output = ""
        self.sn_replacement = set()
        
    def assert_ast(self, input, expected, intermediate=None, expected_sn_replacement=None):

        
        
        def fun(stm):
            if self.print:
                print("--- input -----------------")
                print(inspect_ast(stm))
                print("------------------")
            stm = TRANSFORMERFORTEST.visit(stm)
            self.intermediate += str(inspect_ast(stm)) + "\n"
            stm, sn_repl = make_strong_negations_auxiliar(stm)
            self.sn_replacement.update(sn_repl)
            stm, _ = make_default_negation_auxiliar(stm)
            self.output += str(inspect_ast(stm)) + "\n"
        
        clingo.parse_program(input, fun)
        
        if self.print:
            print("--- intermediate -----------------")
            print(self.intermediate)
        if intermediate is not None:
            self.assertEqual(self.intermediate.replace('\n', '').replace(' ', ''), intermediate.replace('\n', '').replace(' ', ''))
        sn_replacement = str(sorted(self.sn_replacement))
        if self.print:
            print("--- output ----------------------") 
            print(self.output)
            print("--- sn_replacement ----------------------") 
            print(sn_replacement)
        self.assertEqual(self.output.replace('\n', '').replace(' ', ''), expected.replace('\n', '').replace(' ', ''))
        if expected_sn_replacement is not None:
            self.assertEqual(sn_replacement.replace('\n', '').replace(' ', ''), expected_sn_replacement.replace('\n', '').replace(' ', ''))
        

    def test_01(self):
        program = """
            :- &k{ a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a :  }
            TheoryAtom:    &k { a :  }
            Function:    k
            TheoryAtomElement:    a : 
                Literal:    a
                SymbolicAtom:    a
                    Function:    a
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { a :  }.
            Literal:    #false
                BooleanConstant:    #false
            Literal:    &k { a :  }
                TheoryAtom:    &k { a :  }
                Function:    k
                TheoryAtomElement:    a : 
                    Literal:    a
                    SymbolicAtom:    a
                        Function:    a"""
        self.assert_ast(program, expected, intermediate)


    def test_02(self):
        program = """
            :- &k{ - a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { -a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { -a :  }
            TheoryAtom:    &k { -a :  }
            Function:    k
            TheoryAtomElement:    -a : 
                Literal:    -a
                SymbolicAtom:    -a
                    UnaryOperation:    -a
                    Function:    a
        """   
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { sn_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { sn_a :  }
            TheoryAtom:    &k { sn_a :  }
            Function:    k
            TheoryAtomElement:    sn_a : 
                Literal:    sn_a
                SymbolicAtom:    sn_a
                    Function:    sn_a"""
        expected_sn_replacement = str([('a', 0, 'sn_a')])
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_03(self):
        program = """
            :- &k{ - - a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a :  }
            TheoryAtom:    &k { a :  }
            Function:    k
            TheoryAtomElement:    a : 
                Literal:    a
                SymbolicAtom:    a
                    Function:    a
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { a :  }.
            Literal:    #false
                BooleanConstant:    #false
            Literal:    &k { a :  }
                TheoryAtom:    &k { a :  }
                Function:    k
                TheoryAtomElement:    a : 
                    Literal:    a
                    SymbolicAtom:    a
                        Function:    a"""
        self.assert_ast(program, expected, intermediate)


    def test_04(self):
        program = """
            :- &k{ - - - a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { -a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { -a :  }
            TheoryAtom:    &k { -a :  }
            Function:    k
            TheoryAtomElement:    -a : 
                Literal:    -a
                SymbolicAtom:    -a
                    UnaryOperation:    -a
                    Function:    a
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { sn_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { sn_a :  }
            TheoryAtom:    &k { sn_a :  }
            Function:    k
            TheoryAtomElement:    sn_a : 
                Literal:    sn_a
                SymbolicAtom:    sn_a
                    Function:    sn_a"""
        expected_sn_replacement = str([('a', 0, 'sn_a')])
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_05(self):
        program = """
            :- &k{ not a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { not a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not a :  }
            TheoryAtom:    &k { not a :  }
            Function:    k
            TheoryAtomElement:    not a : 
                Literal:    not a
                SymbolicAtom:    a
                    Function:    a"""

        expected = """
        Program:    #program base.

        Rule:    #false :- &k { not_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not_a :  }
            TheoryAtom:    &k { not_a :  }
            Function:    k
            TheoryAtomElement:    not_a : 
                Literal:    not_a
                SymbolicAtom:    not_a
                    Function:    not_a"""
        self.assert_ast(program, expected, intermediate)

    def test_06(self):
        program = """
            :- &k{ not not a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { not not a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not not a :  }
            TheoryAtom:    &k { not not a :  }
            Function:    k
            TheoryAtomElement:    not not a : 
                Literal:    not not a
                SymbolicAtom:    a
                    Function:    a"""

        expected = """
        Program:    #program base.

        Rule:    #false :- &k { not2_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not2_a :  }
            TheoryAtom:    &k { not2_a :  }
            Function:    k
            TheoryAtomElement:    not2_a : 
                Literal:    not2_a
                SymbolicAtom:    not2_a
                    Function:    not2_a"""
        self.assert_ast(program, expected, intermediate)


    def test_07(self):
        program = """
            :- &k{ not -a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { not -a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not -a :  }
            TheoryAtom:    &k { not -a :  }
            Function:    k
            TheoryAtomElement:    not -a : 
                Literal:    not -a
                SymbolicAtom:    -a
                    UnaryOperation:    -a
                    Function:    a"""

        expected = """
        Program:    #program base.

        Rule:    #false :- &k { not_sn_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not_sn_a :  }
            TheoryAtom:    &k { not_sn_a :  }
            Function:    k
            TheoryAtomElement:    not_sn_a : 
                Literal:    not_sn_a
                SymbolicAtom:    not_sn_a
                    Function:    not_sn_a"""
        expected_sn_replacement = str([('a', 0, 'sn_a')])    
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_08(self):
        program = """
            :- &k{ not not -a }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { not not -a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not not -a :  }
            TheoryAtom:    &k { not not -a :  }
            Function:    k
            TheoryAtomElement:    not not -a : 
                Literal:    not not -a
                SymbolicAtom:    -a
                    UnaryOperation:    -a
                    Function:    a"""

        expected = """
        Program:    #program base.

        Rule:    #false :- &k { not2_sn_a :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not2_sn_a :  }
            TheoryAtom:    &k { not2_sn_a :  }
            Function:    k
            TheoryAtomElement:    not2_sn_a : 
                Literal:    not2_sn_a
                SymbolicAtom:    not2_sn_a
                    Function:    not2_sn_a"""
        expected_sn_replacement = str([('a', 0, 'sn_a')])    
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_09(self):
        program = """
            :- &k{ a(2) }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { a(2) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a(2) :  }
            TheoryAtom:    &k { a(2) :  }
            Function:    k
            TheoryAtomElement:    a(2) : 
                Literal:    a(2)
                SymbolicAtom:    a(2)
                    Function:    a(2)
                    Symbol:    2
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { a(2) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a(2) :  }
            TheoryAtom:    &k { a(2) :  }
            Function:    k
            TheoryAtomElement:    a(2) : 
                Literal:    a(2)
                SymbolicAtom:    a(2)
                    Function:    a(2)
                    Symbol:    2"""
        self.assert_ast(program, expected, intermediate)


    def test_10(self):
        program = """
            :- &k{ a(X) }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a(X) :  }
            TheoryAtom:    &k { a(X) :  }
            Function:    k
            TheoryAtomElement:    a(X) : 
                Literal:    a(X)
                SymbolicAtom:    a(X)
                    Function:    a(X)
                    Variable:    X
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { a(X) :  }
            TheoryAtom:    &k { a(X) :  }
            Function:    k
            TheoryAtomElement:    a(X) : 
                Literal:    a(X)
                SymbolicAtom:    a(X)
                    Function:    a(X)
                    Variable:    X"""
        self.assert_ast(program, expected, intermediate)

    def test_11(self):
        program = """
            :- &k{ -a(2) }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { -a(2) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { -a(2) :  }
            TheoryAtom:    &k { -a(2) :  }
            Function:    k
            TheoryAtomElement:    -a(2) : 
                Literal:    -a(2)
                SymbolicAtom:    -a(2)
                    UnaryOperation:    -a(2)
                    Function:    a(2)
                        Symbol:    2
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { sn_a(2) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { sn_a(2) :  }
            TheoryAtom:    &k { sn_a(2) :  }
            Function:    k
            TheoryAtomElement:    sn_a(2) : 
                Literal:    sn_a(2)
                SymbolicAtom:    sn_a(2)
                    Function:    sn_a(2)
                    Symbol:    2"""
        expected_sn_replacement = str([('a', 1, 'sn_a')])
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_12(self):
        program = """
            :- &k{ -a(X) }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { -a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { -a(X) :  }
            TheoryAtom:    &k { -a(X) :  }
            Function:    k
            TheoryAtomElement:    -a(X) : 
                Literal:    -a(X)
                SymbolicAtom:    -a(X)
                    UnaryOperation:    -a(X)
                    Function:    a(X)
                        Variable:    X
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { sn_a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { sn_a(X) :  }
            TheoryAtom:    &k { sn_a(X) :  }
            Function:    k
            TheoryAtomElement:    sn_a(X) : 
                Literal:    sn_a(X)
                SymbolicAtom:    sn_a(X)
                    Function:    sn_a(X)
                    Variable:    X"""
        expected_sn_replacement = str([('a', 1, 'sn_a')])
        self.assert_ast(program, expected, intermediate, expected_sn_replacement)


    def test_13(self):
        program = """
            :- &k{ not a(X) }.
        """
        intermediate = """
        Program:    #program base.

        Rule:    #false :- &k { not a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not a(X) :  }
            TheoryAtom:    &k { not a(X) :  }
            Function:    k
            TheoryAtomElement:    not a(X) : 
                Literal:    not a(X)
                SymbolicAtom:    a(X)
                    Function:    a(X)
                    Variable:    X
        """
        expected = """
        Program:    #program base.

        Rule:    #false :- &k { not_a(X) :  }.
        Literal:    #false
            BooleanConstant:    #false
        Literal:    &k { not_a(X) :  }
            TheoryAtom:    &k { not_a(X) :  }
            Function:    k
            TheoryAtomElement:    not_a(X) : 
                Literal:    not_a(X)
                SymbolicAtom:    not_a(X)
                    Function:    not_a(X)
                    Variable:    X"""
        self.assert_ast(program, expected, intermediate)