from typing import Set
from clingo import Symbol
from eclingo.config import AppConfig
from eclingo.util import clingoext

class Preprocessor():

    def __init__(self,
                 config: AppConfig,
                 control: clingoext.Control) -> None:
        self._control = control
        self._config  = config
        self._epistemic_to_test_mapping = self._control.epistemic_to_test_mapping
        self.facts               = set(self._control.facts())
        self._epistemic_facts    = self._generate_epistemic_facts(self._epistemic_to_test_mapping, self.facts)

    def __call__(self):
        self._add_epistemic_facts_to_control()

    def _generate_epistemic_facts(self, epistemic_to_test, facts) -> Set[Symbol]:
        epistemic_facts: Set[Symbol] = set()
        for epistemic_literal, test_literal in epistemic_to_test.items():
            if test_literal in facts:
                epistemic_facts.add(epistemic_literal)
        return epistemic_facts

    def _add_epistemic_facts_to_control(self):
        with self._control.symbolic_backend() as backend:
            for fact in self._epistemic_facts:
                backend.add_rule([fact], [], [], False)
            # self._control.cleanup()
