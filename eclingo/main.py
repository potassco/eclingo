import clingo
from eclingo.preprocessor.preprocessor import G91Preprocessor, K14Preprocessor
from eclingo.parser.parser import Parser
from eclingo.solver.solver import Solver
from eclingo.postprocessor.postprocessor import Postprocessor


__version__ = '1.0.0'
__optimization__ = 1


class Control:

    def __init__(self, max_models, semantics, optimization):
        self.models = 0
        self.max_models = max_models
        self.semantics = semantics
        self.optimization = optimization
        self._candidates_gen = clingo.Control(['0', '--project'])
        self._candidates_test = clingo.Control(['0'])
        self._epistemic_atoms = {}
        self._predicates = set()
        self._show_signatures = set()

    def add(self, program):
        if self.semantics:
            preprocessor = K14Preprocessor(self._candidates_gen, self._candidates_test)
        else:
            preprocessor = G91Preprocessor(self._candidates_gen, self._candidates_test)

        preprocessor.preprocess(program)
        self._predicates = self._predicates | preprocessor.predicates
        self._show_signatures = self._show_signatures | preprocessor.show_signatures

        del preprocessor

    def add_const(self, name, value):
        self.add('#const {name}={value}.'.format(name=name, value=value))

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

        for model in solver.solve():
            self.models += 1
            yield postprocessor.postprocess(model)

        del solver
        del postprocessor
