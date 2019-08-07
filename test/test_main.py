import support.support as support
import src.preprocesser.preprocesser as preprocesser
import src.solver.solver as solver

INPUT_PROG_PATH = 'test/prog/input/'
OUTPUT_PROG_PATH = 'test/prog/output/'

KB_ELIGIBLE_PATH = 'test/eligible/eligible.lp'
INPUT_ELIGIBLE_PATH = 'test/eligible/input/'
OUTPUT_ELIGIBLE_PATH = 'test/eligible/output/'


def test_prog():
    for i in range(1, 8):
        input_path = INPUT_PROG_PATH + ('prog%02d.lp' % i)
        candidates_gen, candidates_test, epistemic_atoms = preprocesser.parse([input_path])
        result = [model for model in
                  solver.solve(candidates_gen, candidates_test, epistemic_atoms, 0)]
        pretty_result = support.formalize(result)
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as myfile:
            sol = myfile.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert pretty_result == sol


def test_eligible():
    for i in range(1, 17):
        input_path = INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i)
        candidates_gen, candidates_test, epistemic_atoms = preprocesser.parse([KB_ELIGIBLE_PATH, input_path])
        result = [model for model in
                  solver.solve(candidates_gen, candidates_test, epistemic_atoms, 0)]
        pretty_result = support.formalize(result)
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as myfile:
            sol = myfile.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert pretty_result == sol
