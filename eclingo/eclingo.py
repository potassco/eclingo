import sys
import argparse
from timeit import default_timer as timer
from parser import parser
from solver import solver


ECLINGO_VERSION = '1.0.0'


class Eclingo():

    def __init__(self):
        self.elapsed_time = None
        self.version = ECLINGO_VERSION
        self.argparser = argparse.ArgumentParser(prog='eclingo')
        self._set_argparser_args()

    def _set_argparser_args(self):
        self.argparser.add_argument('-n', '--models', type=int,
                                    help='maximum number of models to compute (0 computes all models)',
                                    default=1)
        self.argparser.add_argument('-k', '--k14', action='store_true',
                                    help='computes world views under K14 semantics')
        self.argparser.add_argument('-op', '--optimization', type=int,
                                    help='number of optimization to use (0 for no optimizations)',
                                    default=1)
        self.argparser.add_argument('-c', '--const', action='append',
                                    help='adds a constant to the program (using \'<id>=<term>\' format)')
        self.argparser.add_argument('input_files', nargs='+', type=str, help='path to input files')

    def print_version(self):
        print('eclingo version {}'.format(self.version))

    def main(self, args):
        eclingo_args = self.argparser.parse_args(args)

        start = timer()

        candidates_gen, candidates_test, \
            epistemic_atoms, show_signatures = parser.parse(eclingo_args.input_files,
                                                            eclingo_args.const,
                                                            eclingo_args.k14,
                                                            eclingo_args.optimization)

        yield from solver.solve(candidates_gen, candidates_test,
                                epistemic_atoms, show_signatures, eclingo_args.models)

        end = timer()

        self.elapsed_time = end - start


if __name__ == "__main__":
    eclingo_control = Eclingo()

    eclingo_control.print_version()
    models = 0
    for model in eclingo_control.main(sys.argv[1:]):
        models += 1
        answer = ('\t').join(['&k{ '+str(atom)+' }' for atom in model if 'aux_' in atom.name])
        answer = answer.replace('aux_', '').replace('not_', '~ ').replace('sn_', '-')
        print('Answer: %s\n%s' % (models, answer))

    if models:
        print('SATISFIABLE\n')
    else:
        print('UNSATISFIABLE\n')
    print('Elapsed time: %.6f s' % eclingo_control.elapsed_time)
