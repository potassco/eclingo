from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Iterator, Sequence, Tuple, Union

import clingo as _clingo
from clingo import MessageCode, Symbol, SymbolicAtom
from clingo import ast as _ast

from eclingo.prefixes import atom_user_name
from eclingo.util import clingoext as _clingoext

from .mappings import EpistemicSymbolToTestSymbolMapping, SymbolToEpistemicLiteralMapping, SymbolToEpistemicLiteralMappingUsingProgramLiterals, SymbolToEpistemicLiteralMappingUsingShowStatements


class ASTParsedObject():
    pass

ASTObject = Union[ASTParsedObject, _ast.AST]  # pylint: disable=no-member


@dataclass(frozen=True)
class ShowStatement(ASTParsedObject):
    name: str
    arity: int
    poistive: bool

class ShowSignature(set):
    pass


class ProgramBuilder(_clingoext.ProgramBuilder):

    def __init__(self, builder, program, show_signature):
        super().__init__(builder, program)
        self.show_signature = show_signature

    def add(self, statement: ASTObject):
        if isinstance(statement, ShowStatement):
            self.show_signature.add(statement)
        elif isinstance(statement, _ast.AST): # pylint: disable=no-member
            return super().add(statement)
        else:
            raise RuntimeError("Non recognised object: " + str(statement))


class InternalStateControl(_clingoext.Control):

    def __init__(self, arguments: Iterable[str] = (), logger: Callable[[MessageCode, str], None] = None, message_limit: int = 20, *, control: _clingo.Control = None):
        super().__init__(arguments, logger, message_limit, control=control)
        self.show_signature = ShowSignature()
        self.epistemic_to_test_mapping = EpistemicSymbolToTestSymbolMapping()
        self.show_mapping = SymbolToEpistemicLiteralMapping()

    def builder(self) -> ProgramBuilder:
        return ProgramBuilder(self.control.builder(), self.parsed_program, self.show_signature)

    def show_symbolic_atoms(self) -> Iterator[SymbolicAtom]:
        for show_statement in self.show_signature:
            symbolic_atoms = self.control.symbolic_atoms
            show_statment_user_name = atom_user_name(show_statement.name)
            yield from symbolic_atoms.by_signature(show_statment_user_name, show_statement.arity, show_statement.poistive)

    def show_symbols(self) -> Iterator[Symbol]:
        for symbolic_atom in self.show_symbolic_atoms():
            yield symbolic_atom.symbol

    def ground(self, parts: Iterable[Tuple[str, Iterable[Symbol]]], context: Any = None) -> None:
        super().ground(parts, context)
        self.epistemic_to_test_mapping = EpistemicSymbolToTestSymbolMapping(self)
        self.show_mapping = self._generate_show_mapping()

    def _generate_show_mapping(self) -> SymbolToEpistemicLiteralMapping:
        if self.show_signature:
            return SymbolToEpistemicLiteralMappingUsingShowStatements(self.show_symbols())
        else:
            return SymbolToEpistemicLiteralMappingUsingProgramLiterals(self.epistemic_to_test_mapping.epistemic_literals())




class Application(object):

    @abstractmethod
    def main(self, control: InternalStateControl, files: Sequence[str]) -> None:
        raise NotImplementedError


class ApplicationWrapper(_clingoext.ApplicationWrapper):

    def main(self, control: _clingo.Control, files: Sequence[str]) -> None:
        internal_control = InternalStateControl(control=control)
        return self.application.main(internal_control, files)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self.application, attr)


def clingo_main(application: Application, files: Iterable[str] = ()) -> int:
    application_wrapper = ApplicationWrapper(application)
    return _clingo.clingo_main(application_wrapper, files)
