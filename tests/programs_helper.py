from typing import List, NamedTuple, Optional

from clingo import Symbol

from eclingo.solver.candidate import Candidate


class Program(NamedTuple):
    program: Optional[str]
    non_ground_reification: Optional[str] = None
    ground_reification: Optional[str] = None
    candidates_00_str: Optional[List[str]] = None
    candidates_00: Optional[List[Candidate]] = None
    candidates_01_str: Optional[List[str]] = None
    candidates_01: Optional[List[Candidate]] = None
    candidates_02_str: Optional[List[str]] = None
    candidates_02: Optional[List[Candidate]] = None
    candidates_03_str: Optional[List[str]] = None
    candidates_03: Optional[List[Candidate]] = None
    candidates_wv_str: Optional[List[str]] = None
    candidates_wv: Optional[List[Candidate]] = None
    fast_preprocessing_str: Optional[tuple[str, str]] = None
    fast_preprocessing: Optional[tuple[list[Symbol], list[Symbol]]] = None
    has_fast_preprocessing: bool = False
    description: str = ""
