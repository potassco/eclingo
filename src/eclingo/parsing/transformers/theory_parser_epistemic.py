# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=import-error
import sys
from copy import copy
from typing import Iterable, List, Set, Tuple, Union, cast

from clingo import ast
from clingo.ast import AST, ASTSequence, Sign, TheoryFunction, Transformer
from clingox.ast import (
    filter_body_literals,
    reify_symbolic_atoms,
    theory_term_to_literal,
)

from eclingo.parsing.transformers.astutil import negate_literal

from .parser_negations import (
    SnReplacementType,
    default_negation_auxiliary_rule_replacement,
    make_default_negation_auxiliar,
    make_strong_negations_auxiliar,
)

####################################################################################

# pylint: disable=unused-argument
# pylint: disable=invalid-name


class ApplyToEpistemicAtomsElementsTransformer(Transformer):
    def __init__(self, fun, update_fun=None):
        self.fun = fun
        self.update_fun = update_fun

    def visit_TheoryAtom(self, atom, loc="body"):
        if atom.term.name in {"k", "m"} and not atom.term.arguments:
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


class OldEclingoNegation(Transformer):
    def __init__(self):
        self.in_theory_atom = False

    def visit_TheoryFunction(self, fun, loc="body"):
        if fun.name != "~":
            return fun
        return TheoryFunction(fun.location, "not", fun.arguments)


####################################################################################


def _theory_term_to_literal_adapter(element: AST) -> AST:
    assert len(element.terms) == 1
    old_eclingo_negation_parser = OldEclingoNegation()
    element = old_eclingo_negation_parser.visit(element)
    new_element = copy(element)
    new_element.terms[0] = theory_term_to_literal(element.terms[0])
    return new_element


def parse_epistemic_literals_elements(rule):
    return ApplyToEpistemicAtomsElementsTransformer(_theory_term_to_literal_adapter)(
        rule
    )


####################################################################################


def make_strong_negation_auxiliar_in_epistemic_literals(
    stm: Iterable[ast.AST],
) -> Tuple[Iterable[ast.AST], SnReplacementType]:
    """
    Replaces strong negation by an auxiliary atom inside epistemic literals.
    Returns a pair:
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the name of the strogly negated atom
      * the second element is its arity
      * the third element is the name of the auxiliary atom that replaces it
    """
    replacement: SnReplacementType = set()
    trn = ApplyToEpistemicAtomsElementsTransformer(
        make_strong_negations_auxiliar, replacement.update
    )
    stm = trn.visit_sequence(cast(ASTSequence, stm))
    return (stm, replacement)


####################################################################################


def make_default_negation_auxiliar_in_epistemic_literals(
    stm: Iterable[ast.AST],
) -> Tuple[Iterable[ast.AST], Iterable[ast.AST]]:
    """
    Replaces default negation by an auxiliary atom inside epistemic literals.
    Returns a pair:
    - the first element is the result of such replacement
    - the second element is a set of triples containing information about the replacement:
      * the first element is the auxiliary literal replacing the negated literal
      * the second element is the original literal replaced
    """
    replacement: Set[ast.AST] = set()
    trn = ApplyToEpistemicAtomsElementsTransformer(
        make_default_negation_auxiliar,
        lambda x: replacement.add(x) if x is not None else None,
    )
    stm = trn.visit_sequence(cast(ASTSequence, stm))
    return (stm, replacement)


####################################################################################


def build_guard(body):
    return list(
        filter_body_literals(
            body,
            theory_atom_predicate=lambda x: x.elements[0].terms[0].sign == Sign.NoSign,
        )
    )


####################################################################################


class EpistemicLiteralNegationsToAuxiliarTransformer(Transformer):
    def __init__(self, user_prefix="u"):
        self.user_prefix = user_prefix
        self.sn_replacement = set()
        self.aux_rules = []

    def visit_Rule(self, rule):
        head = rule.head
        body = rule.body
        body, self.sn_replacement = make_strong_negation_auxiliar_in_epistemic_literals(
            body
        )
        guard = build_guard(body)
        body, not_replacement = make_default_negation_auxiliar_in_epistemic_literals(
            body
        )
        self.aux_rules.extend(
            default_negation_auxiliary_rule_replacement(
                rule.location, not_replacement, guard
            )
        )
        return ast.Rule(rule.location, head, body)


####################################################################################


def replace_negations_by_auxiliary_atoms_in_epistemic_literals(
    stm: ast.AST, user_prefix: str = "u"
) -> Tuple[List[ast.AST], SnReplacementType]:
    """
    Replaces strong and default negations by an auxiliary atom inside epistemic literals of the rule.

    user_prefix is preapend to the name of all symbols to avoid collisions with the axiliary atoms.

    Returns a triple:
    - the first element is the result of such replacement
    - the second element is a list of rules relating the auxiliary atoms used to replace default negation with their original literals
    - the third element contains the information about the replacements corresponding to strong negation
    """
    trn = EpistemicLiteralNegationsToAuxiliarTransformer(user_prefix)
    rule = trn.visit(stm)
    return ([rule] + trn.aux_rules, trn.sn_replacement)


####################################################################################


def ensure_literal(stm):
    assert stm.ast_type != ast.ASTType.SymbolicTerm
    assert stm.ast_type != ast.ASTType.Function
    if stm.ast_type == ast.ASTType.SymbolicAtom:
        stm = ast.Literal(stm.symbol.location, ast.Sign.NoSign, stm)
    return stm


def ensure_literals(stms):
    if isinstance(stms, ast.AST):
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
            for nested_literal, aux_atom in self.epistemic_replacements:
                conditional_literal = ast.ConditionalLiteral(
                    x.location, ensure_literal(aux_atom), []
                )
                aux_rule_head = ast.Aggregate(
                    x.location, None, [conditional_literal], None
                )
                aux_rule = ast.Rule(x.location, aux_rule_head, [nested_literal])
                self.aux_rules.append(aux_rule)
        return x

    def visit_TheoryAtom(self, atom, loc="body"):
        assert atom.term.name in {"k", "m"} and not atom.term.arguments
        nested_literal = atom.elements[0].terms[0]

        aux_atom = reify_symbolic_atoms(
            nested_literal.atom, atom.term.name, reify_strong_negation=False
        )

        self.epistemic_replacements.append((nested_literal, aux_atom))
        return aux_atom


def _replace_epistemic_literals_by_auxiliary_atoms(
    stm: ast.AST, k_prefix: str = "k"
) -> List[ast.AST]:
    trans = EClingoTransformer(k_prefix)
    rule = trans(stm)
    rules = [rule] + trans.aux_rules
    return rules


def replace_epistemic_literals_by_auxiliary_atoms(
    stms: Iterable[ast.AST], k_prefix: str = "k"
) -> List[ast.AST]:
    rules = []
    for stm in stms:
        rules.extend(_replace_epistemic_literals_by_auxiliary_atoms(stm, k_prefix))
    return rules


####################################################################################


class MTransformer(Transformer):

    def visit_Literal(self, stm, loc="body"):
        if (
            stm.atom.ast_type != ast.ASTType.TheoryAtom
            or stm.atom.term.name != "m"
            or stm.atom.term.arguments
        ):
            return stm
        literal = negate_literal(stm.atom.elements[0].terms[0])
        stm = negate_literal(stm)
        stm.atom.elements[0].terms[0] = literal
        stm.atom.term.name = "k"
        return stm


def parse_m_literals(stm: AST) -> AST:
    transformer = MTransformer()
    return transformer.visit(stm)


####################################################################################


class G94Transformer(Transformer):

    def visit_Literal(self, stm, loc="body"):
        is_nonnegative_epistemic_listeral = (
            (stm.sign == Sign.NoSign)
            and (stm.atom.ast_type == ast.ASTType.TheoryAtom)
            and (stm.atom.term.name == "k")
            and (not stm.atom.term.arguments)
        )
        if is_nonnegative_epistemic_listeral:
            return ast.Literal(stm.location, Sign.DoubleNegation, stm.atom)
        return stm


def double_negate_epistemic_listerals(stm):
    transformer = G94Transformer()
    return transformer.visit(stm)
