"""
Module with functions to transform theory elements into literals.
"""
import clingo as _clingo
from clingo import ast as _ast
from . import astutil as _astutil

# pylint: disable=all

# {{{1 parse_raw_formula

from clingo.ast import Transformer

class TheoryParser:
    """
    Parser for literals.

    Constants:
    unary  -- Boolean to mark unary operators.
    binary -- Boolean to mark unary operators.
    left   -- Boolean to mark left associativity.
    right  -- Boolean to mark right associativity.
    """
    unary, binary = True, False
    left,  right  = True, False
    table = {
        ("not", unary):  (7, None),
        ("~"  , unary):  (7, None),
        ("-"  , unary):  (7, None)
    }

    def __init__(self):
        """
        Initializes the parser.
        """
        self.__stack  = []

    def __priority_and_associativity(self, operator):
        """
        Get priority and associativity of the given binary operator.
        """
        return self.table[(operator, self.binary)]

    def __priority(self, operator, unary):
        """
        Get priority of the given unary or binary operator.
        """
        return self.table[(operator, unary)][0]

    def __check(self, operator):
        """
        Returns true if the stack has to be reduced because of the precedence
        of the given binary operator is lower than the preceeding operator on
        the stack.
        """
        if len(self.__stack) < 2:
            return False
        priority, associativity = self.__priority_and_associativity(operator)
        previous_priority       = self.__priority(*self.__stack[-2])
        return previous_priority > priority or (previous_priority == priority and associativity)

    def __reduce(self):
        """
        Combines the last unary or binary term on the stack.
        """
        b = self.__stack.pop()
        operator, unary = self.__stack.pop()
        if unary:
            self.__stack.append(_ast.TheoryFunction(b.location, operator, [b]))
        else:
            a = self.__stack.pop()
            l = {"begin": a.location["begin"], "end": b.location["end"]}
            self.__stack.append(_ast.TheoryFunction(l, operator, [a, b]))

    def parse(self, x):
        """
        Parses the given unparsed term, replacing it by nested theory
        functions.
        """
        del self.__stack[:]
        unary = True
        for element in x.elements:
            for operator in element.operators:
                if not (operator, unary) in self.table:
                    raise RuntimeError("invalid operator in: {}".format(x.location))
                while not unary and self.__check(operator):
                    self.__reduce()
                self.__stack.append((operator, unary))
                unary = True
            self.__stack.append(element.term)
            unary = False
        while len(self.__stack) > 1:
            self.__reduce()
        return self.__stack[0]

def parse_raw_formula(x):
    """
    Turns the given unparsed term into a term.
    """
    return TheoryParser().parse(x)

# {{{1 theory_term -> term

class TheoryTermToTermTransformer(Transformer):
    """
    This class transforms a given theory term into a plain term.
    """
    def visit_TheoryTermSequence(self, x):
        """
        Theory term tuples are mapped to term tuples.
        """
        if x.sequence_type == _ast.TheorySequenceType.Tuple:
            return _ast.Function(x.location, "", [self(a) for a in x.arguments], False)
        else:
            raise RuntimeError("invalid term: {}".format(x.location))

    def visit_TheoryFunction(self, x):
        """
        Theory functions are mapped to functions.

        If the function name refers to a function in the table, an exception is thrown.
        """
        isnum = lambda y: y.type == _ast.ASTType.Symbol and y.symbol.type == _clingo.SymbolType.Number
        if x.name == "-" and len(x.arguments) == 1:
            rhs = self(x.arguments[0])
            if isnum(rhs):
                return _ast.Symbol(x.location, _clingo.Number(-rhs.symbol.number))
            else:
                return _ast.UnaryOperation(x.location, _ast.UnaryOperator.Minus, rhs)
        elif (x.name == "+" or x.name == "-") and len(x.arguments) == 2:
            lhs = self(x.arguments[0])
            rhs = self(x.arguments[1])
            op  = _ast.BinaryOperator.Plus if x.name == "+" else _ast.BinaryOperator.Minus
            if isnum(lhs) and isnum(rhs):
                lhs = lhs.symbol.number
                rhs = rhs.symbol.number
                return _ast.SymbolicTerm(x.location, _clingo.Number(lhs + rhs if x.name == "+" else lhs - rhs))
            else:
                return _ast.BinaryOperation(x.location, op, lhs, rhs)
        elif x.name == "-" and len(x.arguments) == 2:
            return _ast.BinaryOperation(x.location, _ast.BinaryOperator.Minus, self(x.arguments[0]), self(x.arguments[1]))
        elif (x.name, TheoryParser.binary) in TheoryParser.table or (x.name, TheoryParser.unary) in TheoryParser.table:
            raise RuntimeError("invalid term: {}".format(x.location))
        else:
            return _ast.Function(x.location, x.name, [self(a) for a in x.arguments], False)

    def visit_TheoryUnparsedTerm(self, x):
        """
        Unparsed term are first parsed and then handled by the transformer.
        """
        return self.visit(parse_raw_formula(x))

def theory_term_to_term(x):
    """
    Convert the given theory term into a term.
    """
    return TheoryTermToTermTransformer()(x)

# {{{1 theory_term -> symbolic_atom

class TheoryTermToLiteralTransformer(Transformer):
    """
    Turns the given theory term into an atom.
    """

    def visit_SymbolicTerm(self, x, positive, sign):
        """
        Maps functions to atoms.

        Every other symbol causes a runtime error.

        Arguments:
        x        -- The theory term to translate.
        positive -- The classical sign of the atom.
        """
        symbol = x.symbol
        if x.symbol.type == _clingo.SymbolType.Function and len(symbol.name) > 0:
            atom = _astutil.atom(x.location, positive == symbol.positive, symbol.name, [_ast.Symbol(x.location, a) for a in symbol.arguments])
            return _ast.Literal(x.location, sign, atom)
        else:
            raise RuntimeError("invalid formula: {}".format(x.location))

    def visit_Variable(self, x, positive, sign):
        """
        Raises an error.
        """
        raise RuntimeError("invalid formula: {}".format(x.location))


    def visit_TheoryTermSequence(self, x, positive, sign):
        """
        Raises an error.
        """
        raise RuntimeError("invalid formula: {}".format(x.location))

    def visit_TheoryFunction(self, x, positive, sign):
        """
        Maps theory functions to atoms.

        If the function name is not a negation, an exception is thrown.
        """
        if x.name == "-":
            return self.visit(x.arguments[0], not positive, sign)
        elif positive and (x.name == "not" or x.name == "~"):
            if sign == _ast.Sign.Negation:
                return self.visit(x.arguments[0], positive, _ast.Sign.DoubleNegation)
            else:
                return self.visit(x.arguments[0], positive, _ast.Sign.Negation)
        elif (x.name, TheoryParser.binary) in TheoryParser.table or (x.name, TheoryParser.unary) in TheoryParser.table:
            raise RuntimeError("invalid term: {}".format(x.location))
        else:
            atom = _astutil.atom(x.location, positive, x.name, [theory_term_to_term(a) for a in x.arguments])
            return _ast.Literal(x.location, sign, atom)

    def visit_TheoryUnparsedTerm(self, x, positive, sign):
        """
        Unparsed terms are first parsed and then handled by the transformer.
        """
        return self.visit(parse_raw_formula(x), positive, sign)

def theory_term_to_literal(x, positive=True, sign=_ast.Sign.NoSign):
    """
    Convert the given theory term into an literal.
    """
    return TheoryTermToLiteralTransformer()(x, positive, sign)