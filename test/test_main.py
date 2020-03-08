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
        input_path = INPUT_PROG_PATH + 'prog{:02d}.lp'.format(i)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol{:02d}.txt'.format(i), 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_prog_k14():
    for i in range(1, 8):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=True,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_PROG_PATH + 'prog{:02d}.lp'.format(i)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_PROG_PATH + 'sol{:02d}.txt'.format(i), 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_eligible_g91():
    for i in range(1, 17):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=False,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_ELIGIBLE_PATH + 'eligible{:02d}.lp'.format(i)
        eclingo_control.load(KB_ELIGIBLE_PATH)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible{:02d}.txt'.format(i), 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_eligible_k14():
    for i in range(1, 17):
        eclingo_control = eclingo.Control(max_models=0,
                                          semantics=True,
                                          optimization=eclingo.__optimization__)
        input_path = INPUT_ELIGIBLE_PATH + 'eligible{:02d}.lp'.format(i)
        eclingo_control.load(KB_ELIGIBLE_PATH)
        eclingo_control.load(input_path)
        eclingo_control.parse()
        result = [sorted(model.symbols) for model in eclingo_control.solve()]
        result = str(sorted(result)).replace(' ', '')
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible{:02d}.txt'.format(i), 'r') as output_prog:
            sol = output_prog.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert result == sol


def test_yale_g91():
    for i in range(1, 9):
        if i != 7:
            length = i
            if i == 6:
                length += 1

            eclingo_control = eclingo.Control(max_models=0,
                                              semantics=False,
                                              optimization=eclingo.__optimization__)
            input_path = INPUT_YALE_PATH + 'yale{:02d}.lp'.format(i)
            eclingo_control.load(KB_YALE_PATH)
            eclingo_control.load(input_path)
            eclingo_control.add_const('length', str(length))
            eclingo_control.parse()
            result = [sorted(model.symbols) for model in eclingo_control.solve()]
            result = str(sorted(result)).replace(' ', '')
            with open(OUTPUT_YALE_PATH + 'sol_yale{:02d}.txt'.format(i), 'r') as output_prog:
                sol = output_prog.read()
                sol = sol.replace('\n', '').replace(' ', '')
            assert result == sol
