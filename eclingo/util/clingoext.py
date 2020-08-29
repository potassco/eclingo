import abc
import textwrap as _textwrap
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple, Union

import clingo as _clingo # type: ignore
from clingo import MessageCode, Symbol, TruthValue
from clingo import ast as _ast  # type: ignore # pylint: disable=import-error

from eclingo.util import astutil as _astutil
from eclingo.util.groundprogram import ClingoExternal, ClingoOutputAtom, ClingoProject, ClingoRule, ClingoWeightRule, GroundProgram


class ProgramBuilder():

    def __init__(self, builder, program):
        self.builder = builder
        self.program = program

    def __enter__(self):
        self.builder.__enter__()
        return self

    def __exit__(self, type_, value, traceback):
        return self.builder.__exit__(type_, value, traceback)

    def add(self, statement: _ast.AST): # pylint: disable=no-member
        self.program.append(statement)
        try:
            return self.builder.add(statement)
        except RuntimeError as error:
            if len(error.args) != 1:
                raise error
            if error.args[0] == 'literal expected':
                error.args = ('literal expected, got\n' + _textwrap.indent(_astutil.ast_repr(statement), 13*' '), )
            raise error
        except AttributeError as error:
            if error.args[0] == "'list' object has no attribute 'location'":
                error.args = (error.args[0] + '\n' + _textwrap.indent(_astutil.ast_repr(statement), 13*' '), )
            raise error


class SymbolicBackend():
    def __init__(self, backend):
        self.backend = backend

    def __enter__(self):
        self.backend.__enter__()
        return self

    def __exit__(self, type_, value, traceback):
        return self.backend.__exit__(type_, value, traceback)

    def add_atom(self, symbol: Symbol) -> None:
        self.backend.add_atom(symbol)

    def add_rule(self, head: Iterable[Symbol] = [], pos_body: Iterable[Symbol] = [], neg_body: Iterable[Symbol] = [], choice: bool = False) -> None:  # pylint: disable=dangerous-default-value
        head = list(self._add_symbols_and_return_their_codes(head))
        body = list(self._add_symbols_and_return_their_codes(pos_body))
        body.extend(self._add_symbols_and_return_their_negated_codes(neg_body))
        return self.backend.add_rule(head, body, choice)

    def add_project(self, symbols: Iterable[Symbol]) -> None:
        atoms = list(self._add_symbols_and_return_their_codes(symbols))
        return self.backend.add_project(atoms)

    def _add_symbol_and_return_its_code(self, symbol: Symbol):
        return self.backend.add_atom(symbol)

    def _add_symbols_and_return_their_codes(self, symbols: Iterable[Symbol]):
        return (self._add_symbol_and_return_its_code(symbol) for symbol in symbols)

    def _add_symbols_and_return_their_negated_codes(self, symbols: Iterable[Symbol]):
        return (-x for x in self._add_symbols_and_return_their_codes(symbols))


# class Backend():
#     def __init__(self, backend, program):
#         self.backend = backend
#         self.program = program

#     def __enter__(self):
#         self.backend.__enter__()
#         return self

#     def __exit__(self, type_, value, traceback):
#         return self.backend.__exit__(type_, value, traceback)

#     def add_acyc_edge(self, node_u: int, node_v: int, condition: List[int]) -> None:
#         return self.backend.add_acyc_edge(node_u, node_v, condition)

#     def add_assume(self, literals: List[int]) -> None:
#         self.program.add_assume(literals)
#         return self.backend.add_assume(literals)

#     def add_atom(self, symbol: Optional[Symbol] = None) -> int:
#         if symbol is not None:
#             atom = self.backend.add_atom(symbol)
#             self.program.add(ClingoOutputAtom(symbol, atom))
#         else:
#             atom = self.backend.add_atom()
#         return atom

#     def add_external(self, atom: int, value: TruthValue = TruthValue.False_) -> None:
#         self.program.add_external(atom, value)
#         return self.backend.add_external(atom, value)

#     def add_heuristic(self, atom: int, type_: HeuristicType, bias: int, priority: int, condition: List[int]) -> None:
#         self.program.add_heuristic(atom, type_, bias, priority, condition)
#         return self.backend.add_heuristic(atom, type_, bias, priority, condition)

#     def add_minimize(self, priority: int, literals: List[Tuple[int, int]]) -> None:
#         self.program.add_minimize(priority, literals)
#         return self.backend.add_minimize(priority, literals)

#     def add_project(self, atoms: List[int]) -> None:
#         self.program.add_project(atoms)
#         return self.backend.add_project(atoms)

#     def add_rule(self, head: Iterable[int], body: Iterable[int] = [], choice: bool = False) -> None:  # pylint: disable=dangerous-default-value
#         # self.program.add_rule(choice, list(head), list(body))
#         return self.backend.add_rule(head, body, choice)

#     def add_weight_rule(self, head: Iterable[int], lower: int, body: Iterable[Tuple[int, int]] = [], choice: bool = False) -> None: # pylint: disable=dangerous-default-value
#         self.program.add_weight_rule(choice, list(head), list(body), lower)
#         return self.backend.add_weight_rule(head, lower, body, choice)

#     def add(self, obj: Union[ClingoObject, Iterable[ClingoObject]]) -> None:
#         if isinstance(obj, ClingoRule):
#             self.add_rule(obj.head, obj.body, obj.choice)
#         elif isinstance(obj, ClingoOutputAtom):
#             self.add_atom(obj.symbol)
#         if isinstance(obj, ClingoProject):
#             pass
#             # self.add_projection(obj)
#         elif isinstance(obj, ClingoAssume):
#             pass
#             # self.assumtions.append(obj)
#         elif isinstance(obj, ClingoExternal):
#             pass
#             # self.add_external(obj)
#         elif isinstance(obj, ClingoHeuristic):
#             pass
#             # self.heuristics.append(obj)
#         elif isinstance(obj, ClingoMinimize):
#             pass
#             # self.minimizes.append(obj)
#         elif isinstance(obj, ClingoWeightRule):
#             pass
#             # self.weight_rules.append(obj)
#         elif isinstance(obj, Iterable): # pylint: disable=isinstance-second-argument-not-valid-type
#             for obj2 in obj:
#                 self.add(obj2)



class Control(object):  # type: ignore

    def __init__(self, arguments: Iterable[str] = (), logger: Callable[[MessageCode, str], None] = None, message_limit: int = 20, *, control: _clingo.Control = None):
        if control is None:
            control = _clingo.Control(arguments, logger, message_limit)
        self.control = control
        self.parsed_program: List[_ast.AST] = [] # pylint: disable=no-member
        self.ground_program = GroundProgram()
        self.control.register_observer(Observer(self.ground_program))

    def add_program(self, program: str) -> None:
        with self.builder() as builder:
            _clingo.parse_program(program, builder.add)

    def builder(self) -> ProgramBuilder:
        return ProgramBuilder(self.control.builder(), self.parsed_program)

    def ground(self, parts: Iterable[Tuple[str, Iterable[Symbol]]], context: Any = None) -> None:
        self.control.ground(parts, context)

    def symbolic_backend(self) -> SymbolicBackend:
        return SymbolicBackend(self.control.backend())

    # def backend(self) -> Backend:
    #     return Backend(self.control.backend(), self.ground_program)

    # def register_observer(self, observer, replace: bool = False) -> None:
    #     return super().register_observer(observer, replace)



    def add_to(self, control: Union['Control', _clingo.Control]):
        atoms_gen_to_test_map = dict()
        symbols_and_atoms = []
        with self.control.backend() as backend:
            for name, arity, pos in self.control.symbolic_atoms.signatures:
                for sy_atom in self.control.symbolic_atoms.by_signature(name, arity, pos):
                    atom = backend.add_atom(sy_atom.symbol)
                    symbols_and_atoms.append((sy_atom.symbol, atom))

        # ----------------------------------------------------------------------------------
        def atoms_gen_to_test(backend, literal):
            if literal >= 0:
                atom = literal
                sign = True
            else:
                atom = -literal
                sign = False

            if atom not in atoms_gen_to_test_map:
                test_code = backend.add_atom()
                atoms_gen_to_test_map.update({atom : test_code})

            atom = atoms_gen_to_test_map[atom]

            if not sign:
                atom = -atom
            return atom
        # ----------------------------------------------------------------------------------

        with control.backend() as backend:
            for symbol_and_atom in symbols_and_atoms:
                test_code = backend.add_atom(symbol_and_atom[0])
                atoms_gen_to_test_map.update({symbol_and_atom[1] : test_code})

            for obj in self.ground_program:
                if isinstance(obj, ClingoRule):
                    head = [atoms_gen_to_test(backend, atom) for atom in obj.head]
                    body = [atoms_gen_to_test(backend, atom) for atom in obj.body]
                    backend.add_rule(head, body, obj.choice)
                elif  isinstance(obj, ClingoWeightRule):
                    head = [atoms_gen_to_test(backend, atom) for atom in obj.head]
                    body = [(atoms_gen_to_test(backend, atom_weigth[0]), atom_weigth[1]) for atom_weigth in obj.body]
                    backend.add_weight_rule(head, obj.lower, body, obj.choice)

        return atoms_gen_to_test_map

    def facts(self) -> Iterable[Symbol]:
        for symbolic_atom in self.control.symbolic_atoms:
            if symbolic_atom.is_fact:
                yield symbolic_atom.symbol

    def atom_to_symbol_mapping(self) -> Dict[int, Symbol]:
        mapping = dict()
        for symbolic_atom in self.control.symbolic_atoms:
            if not symbolic_atom.is_fact:
                mapping.update({symbolic_atom.literal : symbolic_atom.symbol})
        return mapping

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self.control, attr)





class Observer(_clingo.Observer):

    def __init__(self, program):
        self.program = program

    def rule(self, choice: bool, head: Sequence[int], body: Sequence[int]) -> None:
        self.program.objects.append(ClingoRule(choice=choice, head=head, body=body))

    def output_atom(self, symbol: Symbol, atom: int) -> None:
        self.program.objects.append(ClingoOutputAtom(symbol=symbol, atom=atom))

    def weight_rule(self, choice: bool, head: Sequence[int], lower_bound: int, body: Sequence[Tuple[int, int]]) -> None:
        self.program.objects.append(ClingoWeightRule(choice, head, body, lower_bound))

    def project(self, atoms: Sequence[int]) -> None:
        self.program.objects.append(ClingoProject(atoms))

    def external(self, atom: int, value: TruthValue) -> None:
        self.program.objects.append(ClingoExternal(atom, value))


class Application(object):

    @abc.abstractmethod
    def main(self, control: Control, files: Sequence[str]) -> None:
        raise NotImplementedError


class ApplicationWrapper(_clingo.Application):
    def __init__(self, application):
        self.application = application

    def main(self, control: _clingo.Control, files: Sequence[str]) -> None:
        ext_control = Control(control=control)
        return self.application.main(ext_control, files)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self.application, attr)


def clingo_main(application: Application, files: Iterable[str] = ()) -> int:
    return _clingo.clingo_main(ApplicationWrapper(application), files)
