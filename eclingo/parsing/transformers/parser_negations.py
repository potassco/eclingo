"""
Module to replace strong and default negations by auxiliary atoms.
"""
from copy import copy
from typing import Iterator, List, Set, Tuple

from clingo import ast  # type: ignore

from . import astutil
from clingo.ast import Transformer, Location, Position

# pylint: disable=all

####################################################################################

class SimplifyStrongNegationsTransformer(Transformer):

    def visit_UnaryOperation(self, x):
        if x.operator_type != ast.UnaryOperator.Minus:
            raise RuntimeError("invalid term: {}".format(x.location))
        elif x.argument.ast_type == ast.ASTType.UnaryOperation:
            if x.argument.operator != '-':
                raise RuntimeError("invalid term: {}".format(x.location))
            else:
                return self.visit(x.argument.argument)
        elif x.argument.ast_type != ast.ASTType.Function:
                raise RuntimeError("invalid term: {}".format(x.location))
        else:
            return x

####################################################################################

def simplify_strong_negations(stm: ast.AST) -> ast.AST:
    """
    Removes duplicate occurrences of strong negation and provides
    an equivalent formula.
    """
    return SimplifyStrongNegationsTransformer().visit(stm)

####################################################################################

class StrongNegationToAuxiliarTransformer(Transformer):

    def __init__(self, strong_negation_prefix="sn"):
        self.strong_negation_prefix = strong_negation_prefix
        self.replacement = set()

    def visit_UnaryOperation(self, x):
        if x.operator_type != ast.UnaryOperator.Minus:
            raise RuntimeError("invalid term: {}".format(x.location))
        elif x.argument.ast_type != ast.ASTType.Function:
            raise RuntimeError("invalid term: {}".format(x.location))
        else:
            x = simplify_strong_negations(x)
            name      = x.argument.name
            location  = x.argument.location
            aux_name  = self.strong_negation_prefix + "_" + name
            arguments = x.argument.arguments
            external  = x.argument.external
            atom      = ast.Function(location, aux_name, arguments, external)
            self.replacement.add((name, len(arguments), aux_name))
            return atom

####################################################################################

class StrongNegationReplacement(Set[Tuple[str, int, str]]):
    
    location = Location(
                    begin=Position(filename='<replace_strong_negation_by_auxiliary_atoms>', line=1, column=1), 
                    end=Position(filename='<replace_strong_negation_by_auxiliary_atoms>', line=1, column=1) 
                )

    def get_auxiliary_rules(self) -> Iterator[ast.AST]:
        """
        Returns a rule of the form:
            aux_name(X1, ..., Xn) :- -name(X1, ... , Xn).
        for each tuple in replacement
        """
        for name, arity, aux_name in self:
            yield self._build_auxliary_rule(name, arity, aux_name)

    def _build_auxliary_rule(self, name: str, arity: int, aux_name: str) -> ast.AST:
        """
        Returns a rule of the form:
            aux_name(X1, ..., Xn) :- -name(X1, ... , Xn).
        where n = arity
        """
        location = StrongNegationReplacement.location
        arguments = []
        for i in range(0, arity):
            var_name = "V" + str(i)
            var = ast.Variable(location, var_name)
            arguments.append(var)
        head = astutil.atom(location, True, aux_name, arguments)
        head = ast.Literal(location, ast.Sign.NoSign, head)
        body_atom = astutil.atom(location, False, name, arguments)
        body = [ast.Literal(location, ast.Sign.NoSign, body_atom)]
        return ast.Rule(location, head, body)

SnReplacementType = Set[Tuple[str, int, str]]

def make_strong_negations_auxiliar(stm: ast.AST) -> Tuple[ast.AST, SnReplacementType]:
    """
    Replaces strong negation by an auxiliary atom.
    Returns a pair: 
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the name of the strogly negated atom
      * the second element is its arity
      * the third element is the name of the auxiliary atom that replaces it
    """
    trn = StrongNegationToAuxiliarTransformer()
    stm = trn.visit(stm)
    return (stm, trn.replacement)


def strong_negation_auxiliary_rule(location, name: str, arity: int, aux_name: str) -> ast.AST:
    """
    Returns a rule of the form:
        aux_name(X1, ..., Xn) :- -name(X1, ... , Xn).
    where n = arity
    """
    arguments = []
    for i in range(0, arity):
        var_name = "V" + str(i)
        var = ast.Variable(location, var_name)
        arguments.append(var)
    head = astutil.atom(location, True, aux_name, arguments)
    head = ast.Literal(location, ast.Sign.NoSign, head)
    body_atom = astutil.atom(location, False, name, arguments)
    body = [ast.Literal(location, ast.Sign.NoSign, body_atom)]
    return ast.Rule(location, head, body)


def strong_negation_auxiliary_rule_replacement(replacement: SnReplacementType) -> Iterator[ast.AST]:
    """
    Returns a rule of the form:
        aux_name(X1, ..., Xn) :- -name(X1, ... , Xn).
    for each tuple in replacement
    """
    location = Location(
                    begin=Position(filename='<transform>', line=1, column=1), 
                    end=Position(filename='<transform>', line=1, column=1) 
                )
    for name, arity, aux_name in replacement:
        yield strong_negation_auxiliary_rule(location, name, arity, aux_name)


####################################################################################


class DefaultNegationsToAuxiliarTransformer(Transformer):

    def __init__(self, default_negation_prefix="not"):
        self.default_negation_prefix = default_negation_prefix
        self.replacement = []

    def visit_Literal(self, x):
        if x.atom.ast_type == ast.ASTType.BooleanConstant:
            return x

        atom = self.visit(x.atom)
        if atom is x.atom and (x.sign == ast.Sign.NoSign):
            return x

        new_x = copy(x)
        new_x.atom = atom

        if new_x.sign == ast.Sign.NoSign:
            return new_x

        if new_x.sign == ast.Sign.Negation:
            sign = self.default_negation_prefix + "_"
        elif new_x.sign == ast.Sign.DoubleNegation:
            sign = self.default_negation_prefix + "2_"
        else:
            sign = ""
       
        location  = atom.symbol.location
        aux_name  = sign + atom.symbol.name
        arguments = atom.symbol.arguments
        external  = atom.symbol.external
        aux_atom  = ast.Function(location, aux_name, arguments, external)
        aux_atom  = ast.SymbolicAtom(aux_atom)
        new_x     = ast.Literal(location, ast.Sign.NoSign, aux_atom)
        
        self.replacement.append((x, new_x))
        return new_x


NotReplacementType = List[Tuple[ast.AST, ast.AST]]

####################################################################################

def make_default_negation_auxiliar(stm: ast.AST) -> Tuple[ast.AST, NotReplacementType]:
    """
    Replaces default negation by an auxiliary atom.
    Returns a pair: 
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the auxiliary literal replacing the negated literal
      * the second element is the original literal replaced
    """
    trn = DefaultNegationsToAuxiliarTransformer()
    stm = trn.visit(stm)
    replacement = trn.replacement
    return (stm, replacement)


def default_negation_auxiliary_rule(location, aux_literal: ast.AST, original_literal: ast.AST, gard: List[ast.AST]) -> ast.AST:
    """
    Returns a rule of the form:
        aux_literal :- gard, original_literal
    """
    rule_body = list(gard)
    rule_body.append(original_literal)
    return ast.Rule(location, aux_literal, rule_body)


def default_negation_auxiliary_rule_replacement(location, replacement: NotReplacementType, gard: List[ast.AST]):
    """
    Returns a rule of the form:
        aux_literal :- gard, original_literal
    for each tuple in replacement
    """
    for original_literal, aux_literal in replacement:
        yield default_negation_auxiliary_rule(location, aux_literal, original_literal, gard)
