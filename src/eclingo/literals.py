from dataclasses import dataclass
from typing import Union

from clingo import Symbol
from clingo.ast import Sign


def sign2str(sign: Sign):
    literal_sign = ""
    if sign == Sign.Negation:
        literal_sign = "not "
    elif sign == Sign.DoubleNegation:
        literal_sign = "not not "
    return literal_sign


@dataclass(eq=True, unsafe_hash=True, order=True)
class Literal:
    atom: Symbol
    sign: Sign

    def __init__(self, atom: Symbol, sign: Sign):
        self.atom = atom
        self.sign = sign

    def __repr__(self):
        return repr(self.sign) + repr(self.atom)

    def __str__(self):
        return sign2str(self.sign) + str(self.atom)


@dataclass(eq=True, unsafe_hash=True, order=True)
class EpistemicLiteral:
    objective_literal: Literal
    sign: Sign = Sign.NoSign
    is_m: bool = False

    def __init__(
        self,
        objective_literal: Union[Literal, Symbol],
        sign: Sign = Sign.NoSign,
        is_m: bool = False,
    ):
        if isinstance(objective_literal, Symbol):
            objective_literal = Literal(objective_literal, Sign.NoSign)
        self.objective_literal = objective_literal
        self.sign = sign
        self.is_m = is_m

    def __str__(self):
        literal_sign = sign2str(self.sign)
        if not self.is_m:
            return f"{literal_sign}&k{{{self.objective_literal}}}"
        else:
            return f"{literal_sign}&m{{{self.objective_literal}}}"
