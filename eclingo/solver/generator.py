import sys
from typing import Iterator

import clingo

from eclingo import internal_states
from eclingo.config import AppConfig

from .candidate import Candidate


class CandidateGenerator():

    def __init__(self, config: AppConfig, control: internal_states.InternalStateControl) -> None:
        self._config = config
        self.control = control
        self._epistemic_literals = self.control.epistemic_to_test_mapping.epistemic_literals()
        with self.control.symbolic_backend() as backend:
            backend.add_project(self._epistemic_literals)

    def __call__(self) -> Iterator[Candidate]:
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                candidate = self.__model_to_candidate(model)
                if self._config.eclingo_verbose > 2:
                    sys.stderr.write(">>> Candidate:\n    Model:%s\n    %s\n" % (model, candidate))
                yield candidate

    def __model_to_candidate(self, model: clingo.Model) -> Candidate:
        candidate_pos = []
        candidate_neg = []
        for epistemic_literal in self._epistemic_literals:
            if model.contains(epistemic_literal):
                candidate_pos.append(epistemic_literal)
            else:
                candidate_neg.append(epistemic_literal)
        return Candidate(candidate_pos, candidate_neg, [], [])
