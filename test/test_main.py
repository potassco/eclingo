import eclingo.main as eclingo


INPUT_PROG_PATH = 'test/prog/input/'
OUTPUT_PROG_PATH = 'test/prog/output/'

KB_ELIGIBLE_PATH = 'test/eligible/eligible.lp'
INPUT_ELIGIBLE_PATH = 'test/eligible/input/'
OUTPUT_ELIGIBLE_PATH = 'test/eligible/output/'

KB_YALE_PATH = 'test/yale/yale.lp'
INPUT_YALE_PATH = 'test/yale/input/'
OUTPUT_YALE_PATH = 'test/yale/output/'


def test_prog_g91():
    for i in range(1, 8):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=False,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_PROG_PATH + f'prog{i:02d}.lp'
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + f'sol{i:02d}.txt', 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_prog_k15():
    for i in range(1, 8):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=True,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_PROG_PATH + f'prog{i:02d}.lp'
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + f'k15_sol{i:02d}.txt', 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_eligible_g91():
    for i in range(1, 17):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=False,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_ELIGIBLE_PATH + f'eligible{i:02d}.lp'
        eclingo_control.load(KB_ELIGIBLE_PATH)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + f'sol_eligible{i:02d}.txt', 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_eligible_k15():
    for i in range(1, 17):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=True,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_ELIGIBLE_PATH + f'eligible{i:02d}.lp'
        eclingo_control.load(KB_ELIGIBLE_PATH)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + f'sol_eligible{i:02d}.txt', 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_yale_g91():
    for i in range(1, 9):
        if i != 6:
            eclingo_control = eclingo.Control(max_models=0,
                                              semantics=False,
                                              optimization=eclingo.__optimization__)
            input_path = INPUT_YALE_PATH + f'yale{i:02d}.lp'
            eclingo_control.load(KB_YALE_PATH)
            eclingo_control.load(input_path)
            eclingo_control.add_const('length', str(i))
            eclingo_control.parse()
            result = [sorted(model.symbols) for model in eclingo_control.solve()]
            result = str(sorted(result)).replace(' ', '')
            with open(OUTPUT_YALE_PATH + f'sol_yale{i:02d}.txt', 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol
