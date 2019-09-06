import argparse
from timeit import default_timer as timer
import src.parser.parser as parser
import src.solver.solver as solver


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-n', '--models', type=int,
                           help='maximum number of models to compute (0 computes all models)',
                           default=1)
    argparser.add_argument('-k', '--k14', action='store_true',
                           help='computes world views under K14 semantics')
    argparser.add_argument('-op', '--optimization', type=int,
                           help='number of optimization to use (0 for no optimizations)',
                           default=1)
    argparser.add_argument('-c', '--const', action='append',
                           help='adds a constant to the program (using \'<id>=<term>\' format)')
    argparser.add_argument('input_files', nargs='+', type=str, help='path to input files')
    args = argparser.parse_args()

    start = timer()

    candidates_gen, candidates_test, \
        epistemic_atoms, show_signatures = parser.parse(args.input_files, args.const,
                                                        args.k14, args.optimization)

    models = 0
    for model in solver.solve(candidates_gen, candidates_test,
                              epistemic_atoms, show_signatures, args.models):
        models += 1
        answer = ('\t').join(['&k{ '+str(atom)+' }' for atom in model if 'aux_' in atom.name])
        answer = answer.replace('aux_', '').replace('not_', '~ ').replace('sn_', '-')
        print('Answer: %s\n%s' % (models, answer))

    end = timer()
    if models:
        print('SATISFIABLE\n')
    else:
        print('UNSATISFIABLE\n')
    print('Elapsed time: %.6f s' % (end - start))


if __name__ == "__main__":
    main()
