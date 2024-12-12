import sys
import time
from typing import Iterable, List, Optional, Sequence, Tuple

from clingo import Symbol
from clingo.ast import AST

from eclingo.config import AppConfig
from eclingo.grounder import Grounder
from eclingo.parsing import parser
from eclingo.solver import SolverReification


def parse_program(stm, parameters=None, name: str = "base") -> List[AST]:
    """Helping function to parse program for flag: --output-e=rewritten"""
    if parameters is None:
        parameters = []
    ret: List[AST] = []
    parser.parse_program(
        stm,
        ret.append,
        parameters,
        name,
        config=AppConfig(semantics="c19-1", verbose=0),
    )
    return ret


class Control(object):
    def __init__(self, control, config=None) -> None:
        # if control is not None:
        self.project = control.configuration.solve.project
        self.max_models = int(control.configuration.solve.models)
        control.configuration.solve.project = "auto,3"
        control.configuration.solve.models = 0
        self.rewritten_program: List[AST] = []
        self.control = control
        if config is None:
            config = AppConfig(semantics="c19-1")
        self.config = config

        if self.max_models == 0:
            self.max_models = sys.maxsize

        self.grounder = Grounder(self.control, self.config)
        self.models = 0
        self.grounded = False
        self.solver: Optional[SolverReification] = None
        self.grounding_time: float = 0
        self.main_grounding_time: float = 0
        self.solving_time: float = 0

    def add_program(self, program) -> None:
        if self.config.eclingo_rewritten == "rewritten":
            self.rewritten_program.extend(parse_program(program))
        else:
            self.grounder.add_program(program)

    def load(self, input_path) -> None:
        with open(input_path, "r") as program:
            self.add_program(program.read())

    def ground(
        self, parts: Sequence[Tuple[str, Sequence[Symbol]]] = (("base", ()),)
    ) -> None:
        start_time = time.time()
        self.grounder.ground(parts)
        self.grounded = True
        self.main_grounding_time += time.time() - start_time
        self.grounding_time += self.main_grounding_time

    def preprocess(self) -> None:
        pass

    def prepare_solver(self) -> None:
        if not self.grounded:
            self.ground()
        start_time = time.time()
        self.solver = SolverReification(self.grounder.reified_facts, self.config)
        self.grounding_time += time.time() - start_time - self.solver.preprocessing_time

    def solve(self):
        if self.solver is None:
            self.prepare_solver()

        start_time = time.time()
        for model in self.solver.solve():
            self.models += 1
            yield model
            if self.models >= self.max_models:
                break
        self.solving_time += time.time() - start_time
        self.solving_time -= self.solver.test_candidate_reification.grounding_time
        self.solver.tester_grounding_time += (
            self.solver.test_candidate_reification.grounding_time
        )
