import contextlib
import io
import os
import subprocess
import sys
import unittest
from unittest.mock import patch

from eclingo.main import main as eclingo_main

# python -m unittest tests.test_app.TestExamples.test_prog_g94

APP_PATH = "../src/eclingo/__main__.py"

INPUT_PROG_PATH = "prog/input/"
OUTPUT_PROG_PATH = "prog/output/"

KB_ELIGIBLE_PATH = "eligible/eligible.lp"
INPUT_ELIGIBLE_PATH = "eligible/input/"
OUTPUT_ELIGIBLE_PATH = "eligible/output/"

KB_YALE_PATH = "yale/yale.lp"
INPUT_YALE_PATH = "yale/input/"
OUTPUT_YALE_PATH = "yale/output/"


def parse_output(output):
    lines = output.split("\n")
    world_views = []
    is_world_view = False
    for line in lines:
        if is_world_view:
            world_view = line.split()
            world_views.append(world_view)
            is_world_view = False
        elif line.startswith("World view:"):
            is_world_view = True
    return world_views


class TestExamples(unittest.TestCase):
    def assert_world_views(
        self, command, input_paths, output_path, external_call=True, use_stdin=False
    ):
        """
        `use_stdin` can be `True` only when `external_call` is also `False`
        """
        assert external_call == False or use_stdin == False
        if not use_stdin:
            command.extend(input_paths)
        if external_call:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            # if process.returncode != 0:
            #     self.fail(f"{command} exit with {process.returncode}\n{stderr.decode('utf-8')}")
            output = stdout.decode("utf-8")
        else:
            if use_stdin:
                program = ""
                for file in input_paths:
                    with open(file) as f:
                        program = program + f.read()
                # command.append("-")
                with (
                    contextlib.redirect_stdout(io.StringIO()) as stdout,
                    patch.object(sys, "argv", command[1:]),
                    patch.object(sys, "stdin", io.StringIO(program)),
                ):
                    eclingo_main()
                    output = stdout.getvalue()
            else:
                with (
                    contextlib.redirect_stdout(io.StringIO()) as stdout,
                    patch.object(sys, "argv", command[1:]),
                ):
                    eclingo_main()
                    output = stdout.getvalue()
        world_views = parse_output(output)
        for world_view in world_views:
            world_view.sort()
        world_views.sort()
        world_views = [str(wv) for wv in world_views]
        world_views = (
            str(world_views).replace(" ", "").replace("'", "").replace('"', "")
        )
        with open(output_path, "r") as output_prog:
            sol = output_prog.read()
            sol = sol.replace("\n", "").replace(" ", "")

        self.assertEqual(world_views, sol, "in " + str(command))

    def test_prog_g94(self):
        for i in range(1, 11):
            path = os.path.dirname(os.path.realpath(__file__))
            input_path = os.path.join(path, INPUT_PROG_PATH)
            input_path = os.path.join(input_path, f"prog{i:02d}.lp")
            output_path = os.path.join(path, OUTPUT_PROG_PATH)
            output_path = os.path.join(output_path, f"sol{i:02d}.txt")
            app_path = os.path.join(path, APP_PATH)

            semantics = "--semantics=g94"
            command = ["python", app_path, semantics, "0"]
            self.assert_world_views(
                command, [input_path], output_path, external_call=False, use_stdin=True
            )
            self.assert_world_views(
                command, [input_path], output_path, external_call=False
            )
            self.assert_world_views(command, [input_path], output_path)

    def test_eligible_g94(self):
        for i in range(1, 17):
            path = os.path.dirname(os.path.realpath(__file__))
            elegible_path = os.path.join(path, KB_ELIGIBLE_PATH)
            input_path = os.path.join(path, INPUT_ELIGIBLE_PATH)
            input_path = os.path.join(input_path, f"eligible{i:02d}.lp")
            output_path = os.path.join(path, OUTPUT_ELIGIBLE_PATH)
            output_path = os.path.join(output_path, f"sol_eligible{i:02d}.txt")
            app_path = os.path.join(path, APP_PATH)

            semantics = "--semantics=g94"
            command = ["python", app_path, semantics, "0"]
            # TODO: Check out why fails if next lines are added (?)
            # self.assert_world_views(
            #     command, [elegible_path, input_path], output_path, external_call=False
            # )
            self.assert_world_views(command, [elegible_path, input_path], output_path)

    def test_yale_g94(self):
        for i in range(1, 9):  # 7 and 8 test -> Not running in decent time.
            if i != 6:
                path = os.path.dirname(os.path.realpath(__file__))
                yale_path = os.path.join(path, KB_YALE_PATH)
                input_path = os.path.join(path, INPUT_YALE_PATH)
                input_path = os.path.join(input_path, f"yale{i:02d}.lp")
                output_path = os.path.join(path, OUTPUT_YALE_PATH)
                output_path = os.path.join(output_path, f"sol_yale{i:02d}.txt")

                app_path = os.path.join(path, APP_PATH)

                semantics = "--semantics=g94"
                constant = "-c length=%d" % i
                command = ["python", app_path, semantics, constant, "0"]
                self.assert_world_views(
                    command, [yale_path, input_path], output_path, external_call=False
                )
                self.assert_world_views(command, [yale_path, input_path], output_path)


class PrintRewrittenTestCase(unittest.TestCase):
    def test_print_rewritten(self):
        command = 'echo "{a}. b :- &k{a}." | eclingo --output-e=rewritten'
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        output = stdout.decode("utf-8")
        self.assertEqual(
            output.strip(),
            """\
{ u(a) }.
u(b) :- k(u(a)).
{ k(u(a)) } :- u(a).""",
        )

    def test_print_rewrittenp_atch(self):
        path = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(path, INPUT_PROG_PATH)
        input_path = os.path.join(input_path, f"prog00.lp")
        command = ["eclingo", input_path, "--output-e=rewritten"]
        with (
            contextlib.redirect_stdout(io.StringIO()) as stdout,
            patch.object(sys, "argv", command),
        ):
            eclingo_main()
            output = stdout.getvalue()
        self.assertEqual(
            output.strip(),
            """\
{ u(a) }.
u(b) :- k(u(a)).
{ k(u(a)) } :- u(a).""",
        )
