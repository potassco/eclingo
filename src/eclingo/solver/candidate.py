import itertools
from typing import NamedTuple, Sequence

from clingo import Symbol


class Assumptions(NamedTuple):
    pos: Sequence[Symbol]
    neg: Sequence[Symbol]

    def __str__(self):  # pragma: no cover
        pos_s = ", ".join(str(s) for s in self.pos)
        neg_s = ", ".join(str(s) for s in self.neg)
        return f"Assumptions(pos=[{pos_s}], neg=[{neg_s}])"


class Candidate(NamedTuple):
    pos: Sequence[Symbol]
    neg: Sequence[Symbol]
    extra_assumptions: Assumptions = Assumptions([], [])

    def __str__(self):  # pragma: no cover
        pos_s = ", ".join(str(s) for s in self.pos)
        neg_s = ", ".join(str(s) for s in self.neg)
        if not self.extra_assumptions.pos and not self.extra_assumptions.neg:
            return f"Candidate(pos=[{pos_s}], neg=[{neg_s}])"
        return f"Candidate(pos=[{pos_s}], neg=[{neg_s}], extra_assumptions={self.extra_assumptions})"

    def proven(self) -> bool:
        return all(
            itertools.chain(
                (a.arguments[0] in self.extra_assumptions.pos for a in self.pos),
                (a.arguments[0] in self.extra_assumptions.neg for a in self.neg),
            )
        )
