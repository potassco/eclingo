# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error
from copy import copy
from typing import Iterable, List, Tuple, Union

import clingo as _clingo
from clingo import ast as _ast
from clingo.ast import Sign

import eclingo.prefixes as _prefixes

from . import astutil as _astutil
from .parser_negations import (NotReplacementType, SnReplacementType,
                               default_negation_auxiliary_rule_replacement,
                               make_default_negation_auxiliar,
                               make_strong_negations_auxiliar)
from .theory_parser_literals import \
    theory_term_to_literal as _theory_term_to_literal

from clingo.ast import Transformer

from clingo.ast import TheoryAtomType, parse_string
####################################################################################

# pylint: disable=unused-argument
# pylint: disable=invalid-name

class ApplyToEpistemicAtomsElementsTransformer(Transformer):

    def __init__(self, fun, update_fun=None):
        self.fun = fun
        self.update_fun = update_fun

    def visit_TheoryAtom(self, atom, loc="body"):
        if atom.term.name == "k" and not atom.term.arguments:
            if self.update_fun is None:
                new_elements = [self.fun(e) for e in atom.elements]
            else:
                new_elements = []
                for element in atom.elements:
                    new_element, update = self.fun(element)
                    new_elements.append(new_element)
                    self.update_fun(update)
            atom.elements = new_elements
            return atom

####################################################################################

def parse_epistemic_literals_elements(rule):
    return ApplyToEpistemicAtomsElementsTransformer(_theory_term_to_literal)(rule)

####################################################################################


def make_strong_negation_auxiliar_in_epistemic_literals(stm: _ast.AST) -> Tuple[_ast.AST, SnReplacementType]:
    """
    Replaces strong negation by an auxiliary atom inside epistemic literals.
    Returns a pair:
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the name of the strogly negated atom
      * the second element is its arity
      * the third element is the name of the auxiliary atom that replaces it
    """
    replacement = set()
    trn = ApplyToEpistemicAtomsElementsTransformer(make_strong_negations_auxiliar, replacement.update)
    stm = trn.visit_sequence(stm)
    return (stm, replacement)


####################################################################################


def make_default_negation_auxiliar_in_epistemic_literals(stm: _ast.AST) -> Tuple[_ast.AST, NotReplacementType]:
    """
    Replaces default negation by an auxiliary atom inside epistemic literals.
    Returns a pair:
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the auxiliary literal replacing the negated literal
      * the second element is the original literal replaced
    """
    replacement = []
    trn = ApplyToEpistemicAtomsElementsTransformer(make_default_negation_auxiliar, replacement.extend)
    stm = trn.visit_sequence(stm)
    return (stm, replacement)


####################################################################################


class TheoryBuildGuard(Transformer):

    def __init__(self, user_prefix="u"):
        self.guard = []
        self.positive = True

    def visit_Literal(self, x, loc="body"):
        if loc != "k":
            self.positive = True
            self.visit(x.atom)
            if self.positive:
                self.guard.append(x)
        elif x.sign != _ast.Sign.NoSign:
            self.positive = False
        return x

    def visit_TheoryAtom(self, atom, loc="body"):
        if atom.term.name == "k" and not atom.term.arguments:
            self.visit_sequence(atom.elements, "k")
        return atom



def build_guard(body):
    t = TheoryBuildGuard()
    t.visit_sequence(body)
    return t.guard


####################################################################################

def _prefix_to_atom_names(prefix, name):
    return prefix + name

class PreapendPrefixTransformer(Transformer):

    def __init__(self, prefix="", skip=None):
        if skip is None:
            skip = set()
        self.prefix = prefix
        self.skip = skip

    def visit_SymbolicTerm(self, stm, loc="body"):
        if stm.symbol.type != _clingo.SymbolType.Function:
            return stm
        if (stm.symbol.name, 0) in self.skip:
            return stm
        return _ast.SymbolicTerm(stm.location, _clingo.Function(_prefix_to_atom_names(self.prefix, stm.symbol.name), [], stm.symbol.positive))

    def visit_Function(self, stm, loc="body"):
        if (stm.name, len(stm.arguments)) in self.skip:
            return stm
        return _ast.Function(stm.location, _prefix_to_atom_names(self.prefix, stm.name), stm.arguments, stm.external)

    def visit_TheoryAtom(self, stm, loc="body"):
        elements = stm.elements
        if stm.term.name == "k" and not stm.term.arguments:
            elements = self.visit_sequence(elements, "k")
        if elements is stm.elements:
            return stm
        return _ast.TheoryAtom(stm.location, stm.term, elements, stm.guard)

    # def visit_Aggregate(self, stm, loc="body"):
    #     elements = self.visit(stm.elements, loc)
    #     if elements is stm.elements:
    #         return stm
    #     return _ast.Aggregate(stm.location, stm.left_guard, elements, stm.right_guard)



####################################################################################


def prefix_to_atom_names(stm, prefix="", skip=None):
    if skip is None:
        skip = set()
    trn = PreapendPrefixTransformer(prefix, skip)
    return trn.visit(stm)


####################################################################################


class EpistemicLiteralNegationsToAuxiliarTransformer(Transformer):

    def __init__(self, user_prefix="u"):
        self.user_prefix = user_prefix
        self.sn_replacement = set()
        self.aux_rules = []

    def visit_Rule(self, rule):
        head = rule.head
        body = rule.body

        body, self.sn_replacement = make_strong_negation_auxiliar_in_epistemic_literals(body)
        guard = build_guard(body)
        body, not_replacement = make_default_negation_auxiliar_in_epistemic_literals(body)
        self.aux_rules.extend(default_negation_auxiliary_rule_replacement(rule.location, not_replacement, guard))
        return _ast.Rule(rule.location, head, body)


####################################################################################


def _replace_negations_by_auxiliary_atoms_in_epistemic_literals(stm: _ast.AST, user_prefix: str ="u") -> Tuple[List[_ast.AST], SnReplacementType]:
    """
    Replaces strong and default negations by an auxiliary atom inside epistemic literals of the rule.

    user_prefix is preapend to the name of all symbols to avoid collisions with the axiliary atoms.

    Returns a triple:
    - the first element is the result of such replacement
    - the second element is a list of rules relating the auxiliary atoms used to replace default negation with their original literals
    - the third element contains the infomration about the replacements corresponding to strong negation
    """
    trn = EpistemicLiteralNegationsToAuxiliarTransformer(user_prefix)
    rule = trn.visit(stm)
    return ([rule] + trn.aux_rules, trn.sn_replacement)


ASTsType = Union[_ast.AST, Iterable[_ast.AST]]

def replace_negations_by_auxiliary_atoms_in_epistemic_literals(stms: ASTsType, user_prefix: str ="u") -> Tuple[List[_ast.AST], SnReplacementType]:
    """
    Replaces strong and default negations by an auxiliary atom inside epistemic literals of the rule.

    user_prefix is preapend to the name of all symbols to avoid collisions with the axiliary atoms.

    Returns a triple:
    - the first element is the result of such replacement
    - the second element is a list of rules relating the auxiliary atoms used to replace default negation with their original literals
    - the third element contains the infomration about the replacements corresponding to strong negation
    """
    if isinstance(stms, _ast.AST):
        return _replace_negations_by_auxiliary_atoms_in_epistemic_literals(stms, user_prefix)
    else:
        rules = []
        replacement = set()
        for stm in stms:
            (new_rules, new_replacement) = _replace_negations_by_auxiliary_atoms_in_epistemic_literals(stm, user_prefix)
            rules.extend(new_rules)
            replacement.update(new_replacement)
        return (rules, replacement)

####################################################################################


def parse_epistemic_literals_negations(stm: _ast.AST, user_prefix: str ="u") -> Tuple[List[_ast.AST], SnReplacementType]:
    """
    Parses epistemic literals and replaces negations by an auxiliary atom inside them.
    The result is an epistemic logic program where all literals inside of epistemic literals are positive.

    user_prefix is preapend to the name of all symbols to avoid collisions with the axiliary atoms.

    Returns a triple:
    - the first element is the result of such replacement
    - the second element is a list of rules relating the auxiliary atoms used to replace default negation with their original literals
    - the third element contains the infomration about the replacements corresponding to strong negation
    """
    # stm = parse_epistemic_literals_elements(stm)
    return replace_negations_by_auxiliary_atoms_in_epistemic_literals(stm, user_prefix)

####################################################################################

def ensure_literal(stm):
    if stm.ast_type == _ast.ASTType.SymbolicTerm or stm.ast_type == _ast.ASTType.Function:
        stm = _ast.SymbolicAtom(stm)
    if stm.ast_type == _ast.ASTType.SymbolicAtom:
        stm = _ast.Literal(stm.symbol.location, _ast.Sign.NoSign, stm)
    return stm

def ensure_literals(stms):
    if isinstance(stms, _ast.AST):
        return ensure_literal(stms)
    else:
        return [ensure_literal(stm) for stm in stms]

class EClingoTransformer(Transformer):

    def __init__(self, k_prefix="k"):
        self.k_prefix = k_prefix
        self.epistemic_replacements = []
        self.aux_rules = []

    def visit_Rule(self, x, loc="body"):  
        head = ensure_literals(self.visit(x.head, loc="head"))
        body = ensure_literals(self.visit_sequence(x.body, loc="body"))
        if head is not x.head or body is not x.body:
            x = copy(x)
            x.head = head
            x.body = body
            for (nested_literal, aux_atom) in self.epistemic_replacements:
                conditional_literal = _ast.ConditionalLiteral(x.location, ensure_literal(aux_atom), [])
                aux_rule_head       = _ast.Aggregate(x.location, None, [conditional_literal], None)
                aux_rule            = _ast.Rule(x.location, aux_rule_head, [nested_literal])
                self.aux_rules.append(aux_rule)

        return x

    def visit_TheoryAtom(self, atom, loc="body"):
        if atom.term.name == "k" and not atom.term.arguments:
            nested_literal = atom.elements[0].terms[0]
            aux_atom = prefix_to_atom_names(nested_literal.atom, _prefixes.EPISTEMIC_PREFIX)
            self.epistemic_replacements.append((nested_literal, aux_atom))
            return aux_atom
        return atom


def _replace_epistemic_literals_by_auxiliary_atoms(stm: _ast.AST, k_prefix: str = "k") -> List[_ast.AST]:
    trans = EClingoTransformer(k_prefix)
    rule = trans(stm)
    rules = [rule] + trans.aux_rules
    return rules

def replace_epistemic_literals_by_auxiliary_atoms(stms: ASTsType, k_prefix: str = "k") -> List[_ast.AST]:
    if isinstance(stms, _ast.AST):
        return _replace_epistemic_literals_by_auxiliary_atoms(stms, k_prefix)
    else:
        rules = []
        for stm in stms:
            rules.extend(_replace_epistemic_literals_by_auxiliary_atoms(stm, k_prefix))
        return rules


####################################################################################


class G94Transformer(Transformer):

    def visit_Literal(self, stm, loc="body"):
        is_nonnegative_epistemic_listeral = (
            (stm.sign == Sign.NoSign) and
            (stm.atom.ast_type == _ast.ASTType.TheoryAtom) and
            (stm.atom.term.name == "k") and
            (not stm.atom.term.arguments)
        )
        if is_nonnegative_epistemic_listeral:
            return _ast.Literal(
                stm.location,
                Sign.DoubleNegation,
                stm.atom
            )
        else:
            return stm

def double_negate_epistemic_listerals(stm):
    transformer = G94Transformer()
    return transformer.visit(stm)
