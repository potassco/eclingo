import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../eclingo')

import eclingo


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
        result = str(sorted([model for model in eclingo_control.main([input_path, '-n', '0'])]))
        result = result.replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_prog_g91():
    for i in range(1, 8):
        with open(INPUT_PROG_PATH + ('prog%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(eclingo.EclingoSemantics.G91, optimization=1)
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
        result = str(sorted([model for model in eclingo_control.main([input_path, '-n', '0', '-k'])]))
        result = result.replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_prog_k14():
    for i in range(1, 8):
        with open(INPUT_PROG_PATH + ('prog%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(eclingo.EclingoSemantics.K14, optimization=1)
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
        result = str(sorted([model for model in eclingo_control.main([input_path, '-n', '0'])]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_eligible_g91():
    for i in range(1, 17):
        with open(INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(eclingo.EclingoSemantics.G91, optimization=1)
        parser.add(program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_eligible_k14():
    for i in range(1, 17):
        eclingo_control = Eclingo()
        input_path = INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i)
        result = str(sorted([model for model in eclingo_control.main([input_path, '-n', '0', '-k'])]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_mod_eligible_k14():
    for i in range(1, 17):
        with open(INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i), 'r') as input_prog:
            program = input_prog.read()

        parser = Parser(eclingo.EclingoSemantics.K14, optimization=1)
        parser.add(program)
        gen, test, ep_atoms, show_sign = parser.parse()

        solver = Solver(gen, test, ep_atoms, show_sign, models=0)
        result = str(sorted([model for model in solver.solve()]))
        result = result.replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol

def test_main_yale_g91():
    for i in range(1, 9):
        if i!= 7:
            eclingo_control = Eclingo()
            input_path = INPUT_YALE_PATH + ('yale%02d.lp' % i)
            result = str(sorted([model for model in eclingo_control.main([input_path, '-n', '0'])]))
            result = result.replace(' ', '')
            with open(OUTPUT_YALE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol

def test_mod_yale_g91():
    for i in range(1, 8):
        if i!=7:
            with open(INPUT_YALE_PATH + ('yale%02d.lp' % i), 'r') as input_prog:
                program = input_prog.read()

            parser = Parser(eclingo.EclingoSemantics.G91, optimization=1)
            parser.add(program)
            gen, test, ep_atoms, show_sign = parser.parse()

            solver = Solver(gen, test, ep_atoms, show_sign, models=0)
            result = str(sorted([model for model in solver.solve()]))
            result = result.replace(' ', '')
            with open(OUTPUT_YALE_PATH + 'sol%02d.txt' % i, 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol
