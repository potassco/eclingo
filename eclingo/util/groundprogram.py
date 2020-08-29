from dataclasses  import dataclass
from collections import namedtuple
from collections.abc import Iterable
from typing import Dict, List, Sequence, Set, Tuple, Union, Iterable as IterableType
from clingo import Symbol, TruthValue, Function
from eclingo.literals import Literal
# from eclingo.util.prettygroundprogram import PrettyGroundProgram


class ClingoObject(object):
    order: int = 0

    def __lt__(self, other):
        if isinstance(other, ClingoObject):
            return self.order < other.order
        raise Exception("Incomparable type")


@dataclass
class ClingoOutputAtom(ClingoObject):
    symbol: Symbol
    atom: int
    order: int = 0

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return (self.symbol, self.atom) < (other.symbol, other.atom)
        return super().__lt__(other)


class ClingoRuleABC(ClingoObject):
    pass


@dataclass
class ClingoRule(ClingoRuleABC):
    choice: bool
    head: Sequence[int]
    body: Sequence[int]
    order: int = 1

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return (self.choice, self.head, self.body) < (other.choice, other.head, other.body)
        return super().__lt__(other)

@dataclass
class ClingoWeightRule(ClingoObject):
    choice: bool
    head: Sequence[int]
    body: Sequence[Tuple[int, int]]
    lower: int
    order: int = 2

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return (self.choice, self.head, self.body, self.lower) < (other.choice, other.head, other.body, other.lower)
        return super().__lt__(other)

@dataclass
class ClingoProject(ClingoObject):
    atoms: Sequence[int]
    order: int = 3

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.atoms < other.atoms
        elif isinstance(other, ClingoObject):
            return self.order < other.order
        raise Exception("Incomparable type")




ClingoExternal   = namedtuple('ClingoExternal', ['atom', 'value'])
ClingoHeuristic  = namedtuple('ClingoHeuristic', ['atom', 'type', 'bias', 'priority', 'condition'])
ClingoMinimize   = namedtuple('ClingoMinimize', ['priority', 'literals'])
# ClingoWeightRule = namedtuple('ClingoWeightRule', ['choice', 'head', 'body', 'lower'])
ClingoAssume     = namedtuple('ClingoAssume', ['literals'])

@dataclass
class GroundProgram():
    objects : List[ClingoObject]

    def __init__(self, objects: IterableType[ClingoObject] = []):  # pylint: disable=dangerous-default-value
        self.objects = list(objects)

    def add_rule(self, choice: bool = False, head: IterableType[int] = [], body: IterableType[int] = []) -> None: # pylint: disable=dangerous-default-value
        self.objects.append(ClingoRule(choice=choice, head=list(head), body=list(body)))

    def add_rules(self, rules: IterableType[ClingoRule]) -> None:
        self.objects.extend(rules)

    def add_project(self, atoms: List[int] = []) -> None: # pylint: disable=dangerous-default-value
        self.objects.append(ClingoProject(list(atoms)))

    def add(self, obj: Union[ClingoObject, IterableType[ClingoObject]]) -> None:
        if isinstance(obj, ClingoObject):
            self.objects.append(obj)
        elif isinstance(obj, Iterable): # pylint: disable=isinstance-second-argument-not-valid-type
            self.objects.extend(obj)

    def pretty(self):
        return PrettyGroundProgram(self.objects)

    def __str__(self):
        return str(self.pretty())

    def __iter__(self):
        return iter(self.objects)

    # def add_external(self, external: Union[External, ClingoExternal]) -> None:
    #     if isinstance(external, ClingoExternal):
    #         external = self._rewrite_external(external)
    #     self.externals.append(external)

    # def add_assume(self, literals: List[int]) -> None:
    #     self.assumtions.append(ClingoAssume(literals))

    # def add_external(self, atom: int, value: TruthValue = TruthValue.False_) -> None:
    #     self.externals.append(ClingoExternal(atom, value))

    # def add_heuristic(self, atom: int, type: HeuristicType, bias: int, priority: int, condition: List[int]) -> None:
    #     self.externals.append(ClingoHeuristic(atom, type, bias, condition))

    # def add_minimize(self, priority: int, literals: List[Tuple[int, int]]) -> None:
    #     self.externals.append(ClingoMinimize(priority, literals))

    # def add_project(self, atoms: List[int]) -> None:
    #     self.externals.append(ClingoProject(atoms))

    # def add_weight_rule(self, head: List[int], lower: int, body: List[Tuple[int, int]], choice: bool = False) -> None:
    #     self.externals.append(ClingoWeightRule(choice, head, body, lower))


    # def as_list(self):
    #     return self.facts + self.rules + self.output_atoms

    # def __repr__(self):
    #     facts = '.\n'.join(repr(x) for x in self.facts)
    #     if facts:
    #         result = facts + '.'
    #     else:
    #         result = ''
    #     if self.cfacts:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.cfacts)
    #     if self.dfacts:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.dfacts)
    #     if self.rules:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.rules)
    #     # if self.output_atoms:
    #     #     if result:
    #     #         result += '\n\n'
    #     #     result += '\n'.join(repr(x) for x in self.output_atoms)
    #     if self.assumtions:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.assumtions)
    #     if self.externals:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.externals)
    #     if self.heuristics:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.heuristics)
    #     if self.minimizes:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.minimizes)
    #     if self.projections:
    #         if result:
    #             result += '\n\n'
    #         result += '\n'.join(repr(x) for x in self.projections)
    #     if self.weight_rules:
    #         result += '\n'.join(repr(x) for x in self.weight_rules)
    #     return result

class PrettyClingoOject:
    pass


class PrettyRule(PrettyClingoOject):

    def __init__(self, choice: bool = False, head: IterableType['Literal'] = [], body: IterableType['Literal'] = []): # pylint: disable=dangerous-default-value
        head = list(head)
        body = list(body)
        self.choice = choice
        self.head   = head
        self.body   = body

    def __repr__(self):
        if self.head:
            head = ', '.join(str(x) for x in self.head)
            if self.choice:
                head = '{' + head + '}'
        else:
            head = ''
        if self.body:
            body = ':- ' + ', '.join(str(x) for x in self.body)
        else:
            body = ''
        if head and body:
            return head + ' ' + body + '.'
        else:
            return head + body + '.'

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return (self.choice, self.head, self.body) < (other.choice, other.head, other.body)
        # elif isinstance(other, ClingoObject):
        #     return self.order < other.order
        raise Exception("Incomparable type")


class PrettyProjection(PrettyClingoOject):

    def __init__(self, atoms: IterableType[Literal]):
        if not isinstance(atoms, set):
            atoms = set(atoms)
        self.atoms = atoms

    def __repr__(self):
        atoms = ','.join(repr(atom) for atom in self.atoms)
        if atoms:
            return '#project ' + atoms  + '.'
        else:
            return '#project.'

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.atoms < other.atoms
        # elif isinstance(other, ClingoObject):
        #     return self.order < other.order
        raise Exception("Incomparable type")


class PrettyExternal(PrettyClingoOject):

    def __init__(self, atom: Literal, value: TruthValue):
        self.atom  = atom
        self.value = value

    def __repr__(self):
        return '#external ' + repr(self.atom) + ' [' + ('True' if self.value else 'False') + '].'

class PrettyGroundProgram():

    def __init__(self, program: IterableType['ClingoObject']):
        self.symbols: Set[Symbol] = set()
        self.atom_to_symbol: Dict[int, Symbol] = dict()
        self.facts:  List[Symbol]  = list()
        self.cfacts: List[PrettyRule]  = list()
        self.dfacts: List[PrettyRule]  = list()
        self.rules : List[PrettyRule]  = list()
        self.projections  : List[PrettyProjection] = list()
        self.assumtions   : List[ClingoAssume]     = list()
        self.externals    : List[PrettyExternal]   = list()
        self.heuristics   : List[ClingoHeuristic]  = list()
        self.minimizes    : List[ClingoMinimize]   = list()
        self.weight_rules : List[ClingoWeightRule] = list()
        self.add(program)

    def add(self, program: IterableType['ClingoObject']) -> None:
        output_atoms: List[ClingoOutputAtom] = []
        others: List['ClingoObject'] = []

        for obj in program:
            if isinstance(obj, ClingoOutputAtom):
                output_atoms.append(obj)
            else:
                others.append(obj)

        for output_atom in output_atoms:
            self.symbols.add(output_atom.symbol)
            if output_atom.atom != 0:
                self.atom_to_symbol.update({output_atom.atom : output_atom.symbol})
            else:
                self.facts.append(output_atom.symbol)

        self._add(others)
        # discard anonymous facts
        self.facts = list(fact for fact in self.facts if fact in self.symbols)


    def _rewrite_rule(self, rule: 'ClingoRule') -> PrettyRule:
        return self._rewrite_rule2(rule.choice, rule.head, rule.body)

    def _rewrite_rule2(self, choice: bool, head, body) -> PrettyRule:
        head = [self._rewrite_literal(literal) for literal in head]
        body = [self._rewrite_literal(literal) for literal in body]
        return PrettyRule(choice, head, body)

    def _rewrite_literal(self, literal) -> Literal:
        if abs(literal) in self.atom_to_symbol:
            lit = self.atom_to_symbol[abs(literal)]
        else:
            i = abs(literal)
            while True:
                lit = Function('x_' + str(i))
                if lit not in self.symbols:
                    break
                i += 1

        return Literal(lit, literal >= 0)

    def __add_rule(self, rule: PrettyRule) -> None:
        if not rule.body and len(rule.head) == 1:
            if rule.choice:
                self.cfacts.append(rule)
            else:
                self.facts.append(next(iter(rule.head)).atom)
        elif not rule.body:
            self.dfacts.append(rule)
        else:
            self.rules.append(rule)

    def add_rule(self, rule: 'ClingoRule') -> PrettyRule:
        pretty_rule = self._rewrite_rule(rule)
        self.__add_rule(pretty_rule)
        return pretty_rule

    def add_rules(self, rules: IterableType['ClingoRule']) -> None:
        for rule in rules:
            self.add_rule(rule)

    def _rewrite_projection(self, projection: 'ClingoProject') -> PrettyProjection:
        return PrettyProjection(self._rewrite_literal(atom) for atom in projection.atoms)

    def add_projection(self, projection: 'ClingoProject') -> None:
        pretty_projection = self._rewrite_projection(projection)
        self.projections.append(pretty_projection)

    def _rewrite_external(self, external: 'ClingoExternal') -> PrettyExternal:
        return PrettyExternal(self._rewrite_literal(external.atom), external.value)

    def add_external(self, external: 'ClingoExternal') -> None:
        pretty_external = self._rewrite_external(external)
        self.externals.append(pretty_external)

    def add_project(self, atoms: List[int]) -> None:
        self.add_projection(ClingoProject(atoms))

    def _add(self, obj: Union['ClingoObject', IterableType['ClingoObject']]) -> None:
        if isinstance(obj, ClingoRule):
            self.add_rule(obj)
        if isinstance(obj, ClingoProject):
            self.add_projection(obj)
        elif isinstance(obj, ClingoAssume):
            self.assumtions.append(obj)
        elif isinstance(obj, ClingoExternal):
            self.add_external(obj)
        elif isinstance(obj, ClingoHeuristic):
            self.heuristics.append(obj)
        elif isinstance(obj, ClingoMinimize):
            self.minimizes.append(obj)
        elif isinstance(obj, ClingoWeightRule):
            self.weight_rules.append(obj)
        elif isinstance(obj, Iterable):
            for obj2 in obj:
                self._add(obj2)

    def sort(self) -> None:
        self.facts.sort()
        self.cfacts.sort()
        self.dfacts.sort()
        self.rules.sort()
        self.projections.sort()
        self.assumtions.sort()
        self.externals.sort()
        self.heuristics.sort()
        self.minimizes.sort()
        self.weight_rules.sort()

    def as_list(self):
        return [ PrettyRule(False, [fact]) for fact in self.facts ] + \
               self.cfacts + \
               self.dfacts + \
               self.rules + \
               self.weight_rules + \
               self.assumtions + \
               self.assumtions + \
               self.heuristics + \
               self.minimizes + \
               self.projections

    def __repr__(self):
        self.sort()
        facts = '.\n'.join(repr(x) for x in self.facts)
        if facts:
            result = facts + '.'
        else:
            result = ''
        if self.cfacts:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.cfacts)
        if self.dfacts:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.dfacts)
        if self.rules:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.rules)
        if self.weight_rules:
            result += '\n'.join(repr(x) for x in self.weight_rules)
        # if self.output_atoms:
        #     if result:
        #         result += '\n\n'
        #     result += '\n'.join(repr(x) for x in self.output_atoms)
        if self.assumtions:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.assumtions)
        if self.externals:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.externals)
        if self.heuristics:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.heuristics)
        if self.minimizes:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.minimizes)
        if self.projections:
            if result:
                result += '\n\n'
            result += '\n'.join(repr(x) for x in self.projections)
        return result
