from eclingo.main import Eclingo
from eclingo.parser.parser import Parser
from eclingo.solver.solver import Solver
from eclingo.parser.semantics import EclingoSemantics


INPUT_PROG_PATH = 'test/prog/input/'
OUTPUT_PROG_PATH = 'test/prog/output/'

KB_ELIGIBLE_PATH = 'test/eligible/eligible.lp'
INPUT_ELIGIBLE_PATH = 'test/eligible/input/'
OUTPUT_ELIGIBLE_PATH = 'test/eligible/output/'

KB_YALE_PATH = 'test/yale/yale.lp'
INPUT_YALE_PATH = 'test/yale/input/'
OUTPUT_YALE_PATH = 'test/yale/output/'


def test_main_prog_g91():
    for i in range(1, 8):
        eclingo_control = Eclingo()
        input_path = INPUT_PROG_PATH + ('prog%02d.lp' % i)
        result = [
            model for model in eclingo_control.main([input_path, '-n', '0'])
            ]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_prog_g91():
    for i in range(1, 8):
        with open(INPUT_PROG_PATH + ('prog%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(EclingoSemantics.G91, optimization=1)
        parser.add(program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_prog_k14():
    for i in range(1, 8):
        eclingo_control = Eclingo()
        input_path = INPUT_PROG_PATH + ('prog%02d.lp' % i)
        result = [
            model for model in eclingo_control.main([input_path, '-n', '0', '-k'])
            ]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_prog_k14():
    for i in range(1, 8):
        with open(INPUT_PROG_PATH + ('prog%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(EclingoSemantics.K14, optimization=1)
        parser.add(program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_eligible_g91():
    for i in range(1, 17):
        eclingo_control = Eclingo()
        input_path = INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i)
        result = [
            model for model in eclingo_control.main([KB_ELIGIBLE_PATH, input_path, '-n', '0'])
            ]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_eligible_g91():
    for i in range(1, 17):
        with open(KB_ELIGIBLE_PATH, 'r') as eligible_kb:
            problem_kb = eligible_kb.read()
        with open(INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(EclingoSemantics.G91, optimization=1)
        parser.add(problem_kb+program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_eligible_k14():
    for i in range(1, 17):
        eclingo_control = Eclingo()
        input_path = INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i)
        result = [
            model for model in eclingo_control.main([KB_ELIGIBLE_PATH, input_path, '-n', '0', '-k'])
            ]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_eligible_k14():
    for i in range(1, 17):
        with open(KB_ELIGIBLE_PATH, 'r') as eligible_kb:
            problem_kb = eligible_kb.read()
        with open(INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(EclingoSemantics.K14, optimization=1)
        parser.add(problem_kb+program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_yale_g91():
    for i in range(1, 9):
        if i != 7:
            length = i
            if i == 6:
                length += 1

            eclingo_control = Eclingo()
            input_path = INPUT_YALE_PATH + ('yale%02d.lp' % i)
            result = [
                model for model in eclingo_control.main([
                    KB_YALE_PATH, input_path, '-n', '0', '-c', 'length={}'.format(length)
                    ])
                ]
            result = str(sorted(result)).replace(' ', '')
            with open(OUTPUT_YALE_PATH + 'sol_yale%02d.txt' % i, 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol

def test_mod_yale_g91():
    for i in range(1, 8):
        if i != 7:
            length = i
            if i == 6:
                length += 1

            with open(KB_YALE_PATH, 'r') as yale_kb:
                problem_kb = yale_kb.read()
            with open(INPUT_YALE_PATH + ('yale%02d.lp' % i), 'r') as input_prog:
                program = input_prog.read()

            parser = Parser(EclingoSemantics.G91, optimization=1)
            parser.add(problem_kb+program)
            parser.add_constant('length')
            gen, test, ep_atoms, show_sign = parser.parse()

            solver = Solver(gen, test, ep_atoms, show_sign, models=0)
            result = str(sorted([model for model in solver.solve()]))
            result = result.replace(' ', '')
            with open(OUTPUT_YALE_PATH + 'sol_yale%02d.txt' % i, 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol
