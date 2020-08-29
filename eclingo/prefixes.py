from clingo import Function, Symbol
from clingo.ast import Sign # pylint: disable=import-error

from eclingo.literals import Literal, EpistemicLiteral

EPISTEMIC_PREFIX = "k_"
NOT_PREFIX  = "not_"
NOT2_PREFIX = "not2_"
SN_PREFIX   = "sn_"
U_PREFIX    = "u_"

def atom_user_name(name: str, *, positive: bool = True) -> str:
    name = "u_" + name
    if positive:
        return name
    else:
        return "sn_" + name

def atom_not_name(name: str) -> str:
    return "not_" + name

def not_symbol(symbol: Symbol) -> Symbol:
    name = atom_not_name(symbol.name)
    return Function(name, symbol.arguments, positive=True)

def original_user_symbol(symbol: Symbol) -> Symbol:
    name = symbol.name
    if not name.startswith(U_PREFIX):
        raise RuntimeError("Symbol %s does not represent an original user literal")
    name = name[len(U_PREFIX):]
    return Function(name, symbol.arguments, symbol.positive)


def symbol_to_epistemic_literal(symbol: Symbol) -> EpistemicLiteral:
    name = symbol.name
    if not name.startswith(EPISTEMIC_PREFIX):
        raise RuntimeError("Symbol %s does not represent an epistemic literal")
    name = name[len(EPISTEMIC_PREFIX):]
    # if symbol is of the form &k{not L} with L an explicit literal
    if name.startswith(NOT_PREFIX):
        name = name[len(NOT_PREFIX):]
        sign = Sign.Negation
    # if symbol is of the form &k{not not L} with L an explicit literal
    elif name.startswith(NOT2_PREFIX):
        name = name[len(NOT2_PREFIX):]
        sign = Sign.DoubleNegation
    # if symbol is of the form &k{L} with L an explicit literal
    else:
        sign = Sign.NoSign

    # L is of the form -a
    symbol_is_explicitely_negated = name.startswith(SN_PREFIX)
    if symbol_is_explicitely_negated:
        name = name[len(SN_PREFIX):]
    name = name[len(U_PREFIX):]

    new_symbol  = Function(name, symbol.arguments, not symbol_is_explicitely_negated)
    literal = Literal(new_symbol, sign)
    return EpistemicLiteral(literal, Sign.NoSign)
