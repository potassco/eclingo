import clingo
from eclingo.preprocessor.preprocessor import G94Preprocessor, K15Preprocessor
from eclingo.parser.parser import Parser
from eclingo.solver.solver import Solver
from eclingo.postprocessor.postprocessor import Postprocessor
from eclingo.utils.logger import logger, silent_logger


__version__ = '0.2.1'
__optimization__ = 3


class Control:

    def __init__(self, max_models=1, semantics=False, optimization=__optimization__):
        self.models = 0
        self.max_models = max_models
        self.semantics = semantics
        self.optimization = optimization
        self._candidates_gen = clingo.Control(['0', '--project'], logger=silent_logger)
        self._candidates_test = clingo.Control(['0'], logger=logger)
        self._epistemic_atoms = {}
        self._predicates = []
        self._show_signatures = set()

    def add(self, program):
        if self.semantics:
            preprocessor = K15Preprocessor(self._candidates_gen, self._candidates_test,
                                           self.optimization)
        else:
            preprocessor = G94Preprocessor(self._candidates_gen, self._candidates_test,
                                           self.optimization)

        preprocessor.preprocess(program)
        self._predicates.extend(preprocessor.predicates)
        self._show_signatures.update(preprocessor.show_signatures)

        del preprocessor

    def add_const(self, name, value):
        self.add(f'#const {name}={value}.')

    def load(self, input_path):
        with open(input_path, 'r') as program:
            self.add(program.read())

    def parse(self):
        parser = Parser(self._candidates_gen, self._candidates_test,
                        self._predicates, self.optimization)

        parser.parse()
        self._epistemic_atoms.update(parser.epistemic_atoms)

        del parser

    def solve(self):
        solver = Solver(self._candidates_gen, self._candidates_test,
                        self._epistemic_atoms, self.max_models)
        postprocessor = Postprocessor(self._candidates_test, self._show_signatures)

        for model, assumptions in solver.solve():
            self.models += 1
            yield postprocessor.postprocess(model, assumptions)

        del solver
        del postprocessor
