from abc import abstractmethod
from typing import Dict, Iterable, Optional  # , Dict

from clingo import Function, Symbol
from clingo.ast import Sign #pylint: disable=import-error

from eclingo import prefixes
from eclingo.literals import EpistemicLiteral, Literal
from eclingo.util import clingoext


class EpistemicSymbolToTestSymbolMapping(dict): # Dict[Symbol, Symbol],

    def __init__(self, control: Optional[clingoext.Control] = None) -> None:
        super().__init__()
        if control is not None:
            for atom in control.symbolic_atoms:
                symbol = atom.symbol
                symbol_is_epistemic_literal = symbol.name.startswith(prefixes.EPISTEMIC_PREFIX)
                if symbol_is_epistemic_literal:
                    test_symbol = self._generate_test_symbol_from_epistemic_symbol(symbol)
                    self.update({symbol: test_symbol})

    def _generate_test_symbol_from_epistemic_symbol(self, symbol: Symbol) -> Symbol:
        test_symbol_name = symbol.name[len(prefixes.EPISTEMIC_PREFIX):]
        return Function(test_symbol_name, symbol.arguments, symbol.positive)

    def epistemic_literals(self) -> Iterable[Symbol]:
        return self.keys()


class SymbolToEpistemicLiteralMapping():

    def __init__(self, symbols: Iterable[Symbol] = ()) -> None:
        self.positive: Dict[Symbol, EpistemicLiteral] = dict()
        self.negative: Dict[Symbol, EpistemicLiteral] = dict()
        self._generate_mappings(symbols)

    def _generate_mappings(self, symbols: Iterable[Symbol]) -> None:
        pass


class SymbolToEpistemicLiteralMappingUsingProgramLiterals(SymbolToEpistemicLiteralMapping):

    def _generate_mappings(self, symbols: Iterable[Symbol]) -> None:
        for epistemic_symbol in symbols:
            show_symbol = prefixes.symbol_to_epistemic_literal(epistemic_symbol)
            if show_symbol.objective_literal.sign != Sign.Negation:
                self.positive.update({epistemic_symbol: show_symbol})
            else:
                show_symbol = self._generate_m_show_symbol_from_epistemic_symbol(show_symbol)
                self.negative.update({epistemic_symbol: show_symbol})

    def _generate_m_show_symbol_from_epistemic_symbol(self, show_symbol: EpistemicLiteral) -> EpistemicLiteral:
        show_symbol_literal = Literal(show_symbol.objective_literal.atom, Sign.NoSign)
        show_symbol = EpistemicLiteral(show_symbol_literal, Sign.NoSign, is_m=True)
        return show_symbol


class SymbolToEpistemicLiteralMappingUsingShowStatements(SymbolToEpistemicLiteralMapping):

    def _generate_mappings(self, symbols: Iterable[Symbol]) -> None:
        for symbol in symbols:
            original_user_symbol  = prefixes.original_user_symbol(symbol)
            epistemic_literal = EpistemicLiteral(original_user_symbol, Sign.NoSign)
            self.positive.update({symbol: epistemic_literal})

            symbolic_atom_not = prefixes.not_symbol(symbol)
            epistemic_literal = EpistemicLiteral(original_user_symbol, Sign.NoSign, is_m=True)
            self.negative.update({symbolic_atom_not: epistemic_literal})
