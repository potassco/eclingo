import support.support as support
import src.g91.g91 as g91

INPUT_PROG_PATH = 'test/g91/input/'
OUTPUT_PROG_PATH = 'test/g91/output/'

KB_ELIGIBLE_PATH = 'test/eligible/eligible.lp'
INPUT_ELIGIBLE_PATH = 'test/eligible/input/'
OUTPUT_ELIGIBLE_PATH = 'test/eligible/output/'


def test_prog():
    for i in range(1, 8):
        input_path = INPUT_PROG_PATH + ('prog%02d.lp' % i)
        result = [model for model in g91.process(0, [input_path])]
        pretty_result = support.formalize(result)
        with open(OUTPUT_PROG_PATH + 'sol%02d.txt' % i, 'r') as myfile:
            sol = myfile.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert pretty_result == sol


def test_eligible():
    for i in range(1, 17):
        input_path = INPUT_ELIGIBLE_PATH + ('eligible%02d.lp' % i)
        result = [model for model in g91.process(0, [KB_ELIGIBLE_PATH, input_path])]
        pretty_result = support.formalize(result)
        with open(OUTPUT_ELIGIBLE_PATH + 'sol_eligible%02d.txt' % i, 'r') as myfile:
            sol = myfile.read()
            sol = sol.replace('\n', '').replace(' ', '')
        assert pretty_result == sol
