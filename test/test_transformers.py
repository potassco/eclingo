import unittest
import clingo
from clingo import ast as _ast
from eclingo.parsing.transformers.theory_parser_epistemic import \
    parse_epistemic_literals_elements as _parse_epistemic_literals_elements

clingo_version = clingo.__version__


def parse_string(statement, fun):
    if clingo_version < '5.5.1':
        return clingo.parse_program(statement, fun)
    return _ast.parse_string(statement, fun)
    
def ast_type(stm):
    if clingo_version < '5.5.1':
        return stm.type
    return stm.ast_type

def theory_atom_element_terms(stm):
    if clingo_version < '5.5.1':
        return stm.tuple
    return stm.terms

class ProgramParser(object):

    def __init__(self):
        self._statements = []

    def _parse_statement(self, statement: _ast.AST) -> None: # pylint: disable=no-member
        self._statements.append(statement)

    def parse_statement(self, statement):
        parse_string(statement, self._parse_statement)

def literal_statment_from_str(s):
    parser = ProgramParser()
    parser.parse_statement(":- " + s)
    return parser._statements[1].body[0]

def theory_atom_statment_from_str(s):
    return literal_statment_from_str(s).atom

class Test(unittest.TestCase):

    def test_epistemic_atom(self):
        statement = theory_atom_statment_from_str("&k{a}.")
        self.assertEqual(len(statement.elements), 1)
        element = statement.elements[0]
        self.assertEqual(ast_type(element), _ast.ASTType.TheoryAtomElement)
        terms = theory_atom_element_terms(element)
        self.assertEqual(len(terms), 1)
        term = terms[0]

        if clingo_version < '5.5.1':
            self.assertEqual(ast_type(term), _ast.ASTType.TheoryUnparsedTerm)
        else:
            self.assertEqual(ast_type(term), _ast.ASTType.SymbolicTerm)

        result = _parse_epistemic_literals_elements(statement)
        self.assertEqual(len(result.elements), 1)
        element = result.elements[0]
        self.assertEqual(ast_type(element), _ast.ASTType.TheoryAtomElement)

        terms = theory_atom_element_terms(element)
        self.assertEqual(len(terms), 1)
        term = terms[0]
        self.assertEqual(ast_type(term), _ast.ASTType.Literal)

