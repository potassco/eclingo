from typing import List, NamedTuple
from clingo import Symbol

class Candidate(NamedTuple):
    pos: List[Symbol]
    neg: List[Symbol]
    test_pos: List[Symbol]
    test_neg: List[Symbol]
    