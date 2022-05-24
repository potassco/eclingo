import sys
from typing import Iterator

from eclingo import internal_states
from eclingo.config import AppConfig
from eclingo.solver.generator import CandidateGenerator
from eclingo.solver.preprocessor import Preprocessor

from .candidate import Candidate
from .preprocessor import Preprocessor
from .tester import CandidateTester
from .world_view_builder import WorldWiewBuilderWithShow


class Solver:

    def __init__(self,
                 control: internal_states.InternalStateControl,
                 config: AppConfig)  -> None:
        self._control = control
        self._config  = config

        self._build_world_view  = WorldWiewBuilderWithShow(self._control)

        self.test_candidate      = CandidateTester(self._config, self._control)
        self.generate_candidates = CandidateGenerator(self._config, self._control)

        self._preprocesor = Preprocessor(self._config, self._control)
        self._preprocesor()

        if self._config.eclingo_verbose > 1:
            self._stderr_write_current_state()


    def solve(self) -> Iterator[Candidate]:
        for candidate in self.generate_candidates():
            if self.test_candidate(candidate):
                yield self._build_world_view(candidate)


    def _stderr_write_current_state(self) -> None:
        sys.stderr.write('-----------------------------------------------------------')
        sys.stderr.write('\n')
        sys.stderr.write('   Generate program')
        sys.stderr.write('\n')
        sys.stderr.write('-----------------------------------------------------------')
        sys.stderr.write('\n')
        sys.stderr.write(str(self.generate_candidates.control.ground_program))
        sys.stderr.write('\n')
        sys.stderr.write('------------------------------------------------------------')
        sys.stderr.write('\n')
        sys.stderr.write('   Test program')
        sys.stderr.write('\n')
        sys.stderr.write('------------------------------------------------------------')
        sys.stderr.write('\n')
        sys.stderr.write(str(self.test_candidate.control.ground_program))
        sys.stderr.write('\n')
        sys.stderr.write('------------------------------------------------------------')
        sys.stderr.write('\n')
