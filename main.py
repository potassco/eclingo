import argparse
import src.g91.g91 as g91


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_program', type=str, help='input program path')
    args = parser.parse_args()

    result = {frozenset(model) for model in g91.process(args.input_program)}
    print(result)


if __name__ == "__main__":
    main()
