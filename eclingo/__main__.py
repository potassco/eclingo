import argparse
from time import perf_counter as timer
import eclingo.main as eclingo


def main():
    print(f'eclingo version {eclingo.__version__}')

    argparser = argparse.ArgumentParser(prog='eclingo')
    argparser.add_argument('-n', '--models', type=int,
                           help='maximum number of models to compute (0 computes all models)',
                           default=1)
    argparser.add_argument('-k', '--k14', action='store_true',
                           help='computes world views under K14 semantics')
    argparser.add_argument('-op', '--optimization', type=int,
                           help='number of optimization to use (0 for no optimizations)',
                           default=eclingo.__optimization__)
    argparser.add_argument('-c', '--const', action='append',
                           help='adds a constant to the program (using \'<name>=<term>\' format)')
    argparser.add_argument('input_files', nargs='+', type=str, help='path to input files')
    args = argparser.parse_args()

    start = timer()

    eclingo_control = eclingo.Control(max_models=args.models,
                                      semantics=args.k14,
                                      optimization=args.optimization)

    for file_path in args.input_files:
        eclingo_control.load(file_path)
    if args.const:
        for constant in args.const:
            name, term = constant.split('=')
            eclingo_control.add_const(name, term)

    eclingo_control.parse()
    print('Solving...')
    for model in eclingo_control.solve():
        print(f'Answer: {eclingo_control.models}\n{model}')

    end = timer()

    print('SATISFIABLE\n') if eclingo_control.models else print('UNSATISFIABLE\n')

    print('Elapsed time: {:.6f} s'.format(end - start))


if __name__ == "__main__":
    main()
