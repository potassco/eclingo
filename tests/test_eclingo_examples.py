import os
import unittest

import clingo
from clingo import Number

import eclingo as _eclingo
from eclingo.control import Control

# python -m unittest tests.test_eclingo_examples.TestExamples.test_yale_g94

INPUT_PROG_PATH = "prog/input/"
OUTPUT_PROG_PATH = "prog/output/"

KB_ELIGIBLE_PATH = "eligible/eligible.lp"
INPUT_ELIGIBLE_PATH = "eligible/input/"
OUTPUT_ELIGIBLE_PATH = "eligible/output/"

KB_YALE_PATH = "yale/yale-parameter.lp"
INPUT_YALE_PATH = "yale/input/"
OUTPUT_YALE_PATH = "yale/output/"


class TestExamples(unittest.TestCase):
    def test_prog_g94(self):
        for i in range(1, 11):
            control = clingo.Control()
            config = _eclingo.config.AppConfig()
            control.configuration.solve.models = 0
            control.configuration.solve.project = "auto,3"
            eclingo_control = Control(control=control, config=config)
            path = os.path.dirname(os.path.realpath(__file__))
            input_path = os.path.join(path, INPUT_PROG_PATH)
            input_path = os.path.join(input_path, f"prog{i:02d}.lp")
            output_path = os.path.join(path, OUTPUT_PROG_PATH)
            output_path = os.path.join(output_path, f"sol{i:02d}.txt")

            eclingo_control.load(input_path)
            eclingo_control.ground()
            result = [
                [str(symbol) for symbol in model.symbols]
                for model in eclingo_control.solve()
            ]
            result = [sorted(model) for model in result]
            result = str(sorted(result)).replace(" ", "").replace("'", "")
            with open(output_path, "r") as output_prog:
                sol = output_prog.read()
                sol = sol.replace("\n", "").replace(" ", "")
            self.assertEqual(result, sol, "in " + input_path)

    def test_eligible_g94(self):
        for i in range(1, 17):
            control = clingo.Control()
            control.configuration.solve.models = 0
            eclingo_control = Control(control=control)
            # eclingo_control.config.eclingo_verbose = 2
            path = os.path.dirname(os.path.realpath(__file__))
            elegible_path = os.path.join(path, KB_ELIGIBLE_PATH)
            input_path = os.path.join(path, INPUT_ELIGIBLE_PATH)
            input_path = os.path.join(input_path, f"eligible{i:02d}.lp")
            output_path = os.path.join(path, OUTPUT_ELIGIBLE_PATH)
            output_path = os.path.join(output_path, f"sol_eligible{i:02d}.txt")

            eclingo_control.load(elegible_path)
            eclingo_control.load(input_path)
            eclingo_control.ground()

            result = [
                [str(symbol) for symbol in model.symbols]
                for model in eclingo_control.solve()
            ]
            result = [sorted(model) for model in result]
            result = str(sorted(result)).replace(" ", "").replace("'", "")
            with open(output_path, "r") as output_prog:
                sol = output_prog.read()
                sol = sol.replace("\n", "").replace(" ", "")
            self.assertEqual(result, sol, "in " + input_path)

    def test_yale_g94(self):
        for i in range(1, 9):
            if i != 6:
                control = clingo.Control(message_limit=0)
                config = _eclingo.config.AppConfig()
                config.eclingo_semantics = "g94"
                control.configuration.solve.project = "auto,3"
                control.configuration.solve.models = 0

                eclingo_control = Control(control=control, config=config)
                # eclingo_control.config.eclingo_verbose = 10

                path = os.path.dirname(os.path.realpath(__file__))
                yale_path = os.path.join(path, KB_YALE_PATH)
                input_path = os.path.join(path, INPUT_YALE_PATH)
                input_path = os.path.join(input_path, f"yale{i:02d}.lp")
                output_path = os.path.join(path, OUTPUT_YALE_PATH)
                output_path = os.path.join(output_path, f"sol_yale{i:02d}.txt")
                eclingo_control.load(yale_path)
                eclingo_control.load(input_path)
                parts = []
                parts.append(("base", []))
                parts.append(("base", [Number(i)]))
                eclingo_control.ground(parts)

                result = [
                    [str(symbol) for symbol in model.symbols]
                    for model in eclingo_control.solve()
                ]
                result = [sorted(model) for model in result]
                result = str(sorted(result)).replace(" ", "").replace("'", "")

                with open(output_path, "r") as output_prog:
                    sol = output_prog.read()
                    sol = sol.replace("\n", "").replace(" ", "")
                self.assertEqual(result, sol, "in " + input_path)
