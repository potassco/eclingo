from typing import List, NamedTuple

from eclingo.literals import EpistemicLiteral

class WorldView(NamedTuple):
    symbols: List[EpistemicLiteral]

    def __str__(self):
        return ' '.join(map(str, sorted(self.symbols)))
