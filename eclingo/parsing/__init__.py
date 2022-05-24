from collections import namedtuple
from typing import Callable, Iterable, List

from clingo import ast

from clingo.ast import Location, Position

from eclingo import prefixes
from eclingo.internal_states import ASTObject, ShowStatement

from .transformers.parser_negations import \
    StrongNegationReplacement as _StrongNegationReplacement
from .transformers.theory_parser_epistemic import \
    double_negate_epistemic_listerals
from .transformers.theory_parser_epistemic import \
    parse_epistemic_literals_elements as _parse_epistemic_literals_elements
from .transformers.theory_parser_epistemic import \
    prefix_to_atom_names as _prefix_to_atom_names
from .transformers.theory_parser_epistemic import \
    replace_epistemic_literals_by_auxiliary_atoms as \
    _replace_epistemic_literals_by_auxiliary_atoms
from .transformers.theory_parser_epistemic import \
    replace_negations_by_auxiliary_atoms_in_epistemic_literals as \
    _replace_negations_by_auxiliary_atoms_in_epistemic_literals

_CallbackType = Callable[[ASTObject], None]



class _ProgramParser(object):

    def __init__(self, program: str, callback: _CallbackType, parameters: List[str] = [], name: str = "base", semantics = "c19-1"): # pylint: disable=dangerous-default-value
        self.initial_location = Location(begin=Position(filename='<string>', line=1, column=1), end=Position(filename='<string>', line=1, column=1))
        self.program  = program
        self.callback = callback
        self.parameters = [ast.Id(self.initial_location, x) for x in parameters] # pylint: disable=no-member
        self.name = name
        self.strong_negation_replacements = _StrongNegationReplacement()
        self.semantics = semantics

    def __call__(self) -> None:
        ast.parse_string(self.program, self._parse_statement)
        for aux_rule in self.strong_negation_replacements.get_auxiliary_rules():
            self.callback(aux_rule)

    def _parse_statement(self, statement: ast.AST) -> None: # pylint: disable=no-member
        statement = _parse_epistemic_literals_elements(statement)
        statement = _prefix_to_atom_names(statement, prefixes.U_PREFIX)
        # this avoids collitions between user predicates and auxiliary predicates
        if statement.ast_type == ast.ASTType.Rule: # pylint: disable=no-member
            for rule in self._parse_rule(statement):
                self.callback(rule)
        elif statement.ast_type == ast.ASTType.Program: # pylint: disable=no-member
            for statement in self._parse_program_statement(statement):
                self.callback(statement)
        elif statement.ast_type == ast.ASTType.ShowSignature: # pylint: disable=no-member
            for stm in self._parse_show_signature_statement(statement):
                self.callback(stm)
        elif statement.ast_type == ast.ASTType.ShowTerm: # pylint: disable=no-member
            raise RuntimeError('syntax error: only show statements of the form "#show atom/n." are allowed.')
        else:
            self.callback(statement)


    def _parse_rule(self, rule: ast.AST) -> Iterable[ast.AST]: # pylint: disable=no-member
        if self.semantics == "g94":
            rule = double_negate_epistemic_listerals(rule)
        (rules, sn_replacement) = _replace_negations_by_auxiliary_atoms_in_epistemic_literals(rule)
        self.strong_negation_replacements.update(sn_replacement) # pylint: disable=no-member

        return _replace_epistemic_literals_by_auxiliary_atoms(rules, prefixes.EPISTEMIC_PREFIX)

    def _parse_program_statement(self, statement: ast.AST) -> List[ast.AST]: # pylint: disable=no-member
        if statement.name != "base" or \
           statement.parameters or \
           statement.location != self.initial_location:
            return [statement]

        if self.name == "base" and not self.parameters:
            return [statement]

        new_statement = ast.Program(statement.location, self.name, self.parameters) # pylint: disable=no-member
        return [statement, new_statement]

    def _parse_show_signature_statement(self, statement: ast.AST) -> List[ShowStatement]: # pylint: disable=no-member
        return [ShowStatement(statement.name, statement.arity, statement.positive)]

#######################################################################################################

def parse_program(program: str, callback: _CallbackType, parameters: List[str] = [], name: str = "base", semantics: str="c19-1") -> None: # pylint: disable=dangerous-default-value
    _ProgramParser(program, callback, parameters, name, semantics)()
