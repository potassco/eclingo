from eclingo import internal_states
import sys
from typing import Dict

from clingo import Symbol

from eclingo.config import AppConfig
from eclingo.util import clingoext

from .candidate import Candidate


class CandidateTester():

    def __init__(self,
                 config: AppConfig,
                 control: internal_states.InternalStateControl):
        self._config     = config
        self._epistemic_to_test = control.epistemic_to_test_mapping
        self.control      = self._generate_control_test(control)

    def _generate_control_test(self, control) -> clingoext.Control:
        control_test          = clingoext.Control(['0'], message_limit=0)
        control.add_to(control_test)
        self._add_choices_for_epistemic_literals_to(control_test)
        control_test.control.configuration.solve.enum_mode = 'cautious' # type: ignore
        return control_test

    def _add_choices_for_epistemic_literals_to(self, control_test: clingoext.Control) -> None:
        with control_test.symbolic_backend() as backend:
            for literal_code in self._epistemic_to_test.keys():
                backend.add_rule([literal_code], [], [], True)
                # if self._config.eclingo_project_test:
                #     backend.add_project(
                #         [self._atoms_gen_to_test(signature.test_atom_code)
                #          for signature in self._epistemic_to_test.values()])


    def __call__(self, candidate: Candidate) -> bool:
        candidate_pos = []
        candidate_neg = []
        candidate_assumptions = []
        for literal in candidate[0]:
            assumption = (literal, True)
            candidate_assumptions.append(assumption)
            literal = self._epistemic_to_test[literal]
            candidate_pos.append(literal)
        for literal in candidate[1]:
            assumption = (literal, False)
            candidate_assumptions.append(assumption)
            literal = self._epistemic_to_test[literal]
            candidate_neg.append(literal)
        self.control.configuration.solve.models  = 0
        self.control.configuration.solve.project = "no"

        with self.control.solve(yield_=True, assumptions=candidate_assumptions) as handle:
            model = None
            for model in handle:
                for atom in candidate_pos:
                    if not model.contains(atom):
                        if self._config.eclingo_verbose > 2:
                            sys.stderr.write(">>> False, '%s' should hold in all models:\n    %s\n\n" % (atom, model))
                        elif self._config.eclingo_verbose > 3:
                            sys.stderr.write(">>> Model: %s\n\n" % model)
                        return False

            if model is None:
                if self._config.eclingo_verbose > 2:
                    sys.stderr.write(">>> False:\n%s\n\n" % "Unsatisfiable")
                return False

            for atom in candidate_neg:
                if model.contains(atom):
                    if self._config.eclingo_verbose > 2:
                        sys.stderr.write(">>> False, '%s' should not hold in some model:\n    %s\n\n" % (atom, model))
                    return False
        if self._config.eclingo_verbose > 2:
            sys.stderr.write(">>> True\n")
        return True
