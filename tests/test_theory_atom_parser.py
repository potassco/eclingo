import unittest
from typing import Optional, cast

import clingo
from clingo import ast
from clingo.ast import (
    AST,
    ASTType,
    Location,
    Position,
    Transformer,
    Variable,
    parse_string,
)
from clingo.symbol import Function
from clingox.ast import theory_parser_from_definition

theory = """#theory eclingo {
    term { not : 0, unary;
           -   : 0, unary
         };
    &k/0 : term, body
}.
"""

theory_parse = None


def extract(stm):
    if stm.ast_type == ASTType.TheoryDefinition:
        global theory_parse
        theory_parse = theory_parser_from_definition(stm)


parse_string(theory, extract)


class Extractor(Transformer):
    """
    Simple visitor returning the first theory term in a program.
    """

    # pylint: disable=invalid-name
    atom: Optional[AST]

    def __init__(self, parse: bool = False):
        self.atom = None
        self.parse = parse

    def visit_TheoryAtom(self, x: AST):
        """
        Extract theory atom.
        """
        if self.parse:
            x = theory_parse(x)
        self.atom = x
        return x


def theory_atom(s: str, mode: int = 0) -> AST:
    """
    Convert string to theory term.
    """
    if mode == 2:
        v = Extractor(parse=True)
    else:
        v = Extractor()

    def visit(stm):
        v(stm)

    if mode == 0 or mode == 2:
        clingo.ast.parse_string(f"{s}.", visit)
    elif mode == 1:
        clingo.ast.parse_string(theory + f"{s}.", visit)
    return cast(AST, v.atom)


location = Location(
    begin=Position(filename="<string>", line=1, column=1),
    end=Position(filename="<string>", line=1, column=1),
)


class TesterCase(unittest.TestCase):
    def test_theory_parse(self):
        theory_atom_str = "&k{ a }"
        element = ast.TheoryAtomElement(
            [ast.SymbolicTerm(location, Function("a", [], True))], []
        )
        result = theory_atom(theory_atom_str).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ a(X) }"
        element = ast.TheoryAtomElement(
            [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])], []
        )
        result = theory_atom(theory_atom_str).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryUnparsedTerm(
                    location,
                    [
                        ast.TheoryUnparsedTermElement(
                            ["not"],
                            ast.TheoryFunction(
                                location, "a", [ast.Variable(location, "X")]
                            ),
                        )
                    ],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str).elements[0]
        self.assertEqual(result, element)

    def test_theory_parse_with_theory(self):
        theory_atom_str = "&k{ a }"
        element = ast.TheoryAtomElement(
            [ast.SymbolicTerm(location, Function("a", [], True))], []
        )
        result = theory_atom(theory_atom_str, mode=1).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ a(X) }"
        element = ast.TheoryAtomElement(
            [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])], []
        )
        result = theory_atom(theory_atom_str, mode=1).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryUnparsedTerm(
                    location,
                    [
                        ast.TheoryUnparsedTermElement(
                            ["not"],
                            ast.TheoryFunction(
                                location, "a", [ast.Variable(location, "X")]
                            ),
                        )
                    ],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=1).elements[0]
        self.assertEqual(result, element)

    def test_theory_parse_with_clingox_theory(self):
        theory_atom_str = "&k{ a }"
        element = ast.TheoryAtomElement(
            [ast.SymbolicTerm(location, Function("a", [], True))], []
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ a(X) }"
        element = ast.TheoryAtomElement(
            [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])], []
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not a }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "not",
                    [ast.SymbolicTerm(location, Function("a", [], True))],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "not",
                    [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ - a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "-",
                    [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not not a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "not",
                    [
                        ast.TheoryFunction(
                            location,
                            "not",
                            [
                                ast.TheoryFunction(
                                    location, "a", [ast.Variable(location, "X")]
                                )
                            ],
                        )
                    ],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ not - a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "not",
                    [
                        ast.TheoryFunction(
                            location,
                            "-",
                            [
                                ast.TheoryFunction(
                                    location, "a", [ast.Variable(location, "X")]
                                )
                            ],
                        )
                    ],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

        theory_atom_str = "&k{ - not a(X) }"
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "-",
                    [
                        ast.TheoryFunction(
                            location,
                            "not",
                            [
                                ast.TheoryFunction(
                                    location, "a", [ast.Variable(location, "X")]
                                )
                            ],
                        )
                    ],
                )
            ],
            [],
        )
        result = theory_atom(theory_atom_str, mode=2).elements[0]
        self.assertEqual(result, element)

    def test_theory_parse_element(self):
        element = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "-",
                    [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])],
                )
            ],
            [],
        )
        result = theory_parse(element)
        expected = ast.TheoryAtomElement(
            [
                ast.TheoryFunction(
                    location,
                    "-",
                    [ast.TheoryFunction(location, "a", [ast.Variable(location, "X")])],
                )
            ],
            [],
        )
        self.assertEqual(element, expected)

    def test_theory_parse_term(self):
        term = ast.TheoryUnparsedTerm(
            Location(
                begin=Position(filename="<string>", line=1, column=7),
                end=Position(filename="<string>", line=1, column=9),
            ),
            [
                ast.TheoryUnparsedTermElement(
                    ["-"],
                    ast.SymbolicTerm(
                        Location(
                            begin=Position(filename="<string>", line=1, column=8),
                            end=Position(filename="<string>", line=1, column=9),
                        ),
                        Function("a", [], True),
                    ),
                )
            ],
        )
        result = theory_parse(term)
        self.assertEqual(term, term)
