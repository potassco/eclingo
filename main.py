import argparse
from timeit import default_timer as timer
import src.preprocesser.preprocesser as preprocesser
import src.solver.solver as solver


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--models', type=int,
                        help='maximum number of models to compute (0 computes all models)',
                        default=1)
    parser.add_argument('input_files', nargs='+', type=str, help='path to input files')
    args = parser.parse_args()

    candidates_gen, candidates_test, epistemic_atoms = preprocesser.parse(args.input_files)

    start = timer()

    for model in solver.solve(candidates_gen, candidates_test, epistemic_atoms, args.models):
        print(model)

    end = timer()
    print('Elapsed time: %.6f' % (end - start))


if __name__ == "__main__":
    main()
