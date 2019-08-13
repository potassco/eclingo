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
    argparser.add_argument('input_files', nargs='+', type=str, help='path to input files')
    args = argparser.parse_args()

    start = timer()

    candidates_gen, candidates_test, epistemic_atoms = parser.parse(args.input_files, args.k14)

    for model in solver.solve(candidates_gen, candidates_test, epistemic_atoms, args.models):
        print([str(atom).replace('aux_', 'K{ ').replace('not_', '~ ').replace('sn_', '-')+' }'
               for atom in model])

    end = timer()
    print('Elapsed time: %.6f' % (end - start))


if __name__ == "__main__":
    main()
