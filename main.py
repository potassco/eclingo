import argparse
import src.g91.g91 as g91


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--models', type=int,
                        help='maximum number of models to compute (0 computes all models)',
                        default=1)
    parser.add_argument('input_files', nargs='+', type=str, help='path to input files')
    args = parser.parse_args()

    result = {frozenset(model) for model in g91.process(args.models, args.input_files)}
    print(result)


if __name__ == "__main__":
    main()
