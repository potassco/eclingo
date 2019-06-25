import argparse
import clingo

THEORY_PATH = "asp/theory/theory.lp"

class Observer:
    def __init__(self):
        self.rules = []

    def rule(self, _choice, head, body):
        self.rules.append((head, body))


class Processor:
    def __init__(self):
        self.symbolic_atoms = []
        self.theory_atoms = []
        self.rules = []
        self.cc = clingo.Control()
        self.backend = None

    def main(self, input_program):
        observer = Observer()

        self.cc.load(input_program)
        self.cc.load(THEORY_PATH)
        self.cc.register_observer(observer, False)
        self.cc.ground([("base", [])])
        self.rules = observer.rules

        self.symbolic_atoms = {x.literal: x.symbol for x in self.cc.symbolic_atoms}
        self.theory_atoms = {x.literal: x.elements[0].terms[0] for x in self.cc.theory_atoms}

        print(self.rules)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_program', type=str, help='input program path')
    args = parser.parse_args()

    processor = Processor()
    processor.main(args.input_program)


if __name__ == "__main__":
    main()
