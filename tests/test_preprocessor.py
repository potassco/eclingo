import textwrap
import unittest
from typing import List

import eclingo
from eclingo.solver.generator import GeneratorReification
from eclingo.solver.tester import CandidateTesterReification
from tests.generated_programs import programs
from tests.parse_programs import parse_program

config = eclingo.config.AppConfig()
config.eclingo_semantics = "c19-1"
config.preprocessing_level = 3
config.propagate = False


def fast_preprocessing(program):
    program = parse_program(program)
    tester = CandidateTesterReification(config, program)
    ret = tester.fast_preprocessing()
    return ret


def generate_candidates(program, preprocessing_result):
    program = parse_program(program)
    generator = GeneratorReification(config, program, preprocessing_result)
    ret = list(generator())
    return ret


def format_subtest_message(i: int, program: str, expected: List[str]) -> str:
    program = textwrap.indent(program, 4 * " ")
    expected = textwrap.indent(str(expected), 4 * " ")
    return f"""\

Program {i}:
{program}
Expected result:
{expected}
"""


class PreprocessorTestCase(unittest.TestCase):
    # def assert_models(self, models, expected):
    # discarding assumptiosn from the comparison
    # models = [Candidate(pos=m.pos, neg=m.neg) for m in models]
    # self.assertCountEqual(models, expected)

    def test_preprocessor(self):
        for i, program in enumerate(programs):
            # print(program.program)
            prg = program.ground_reification
            if prg is not None and program.has_fast_preprocessing:
                with self.subTest(
                    format_subtest_message(
                        i, program.program, program.fast_preprocessing_str
                    )
                ):
                    ret = fast_preprocessing(prg)
                    if program.fast_preprocessing is None:
                        self.assertTrue(ret.unsatisfiable)
                    else:
                        self.assertFalse(ret.unsatisfiable)
                        self.assertCountEqual(
                            [str(a) for a in ret[1]],
                            [str(a) for a in program.fast_preprocessing[0]],
                            "lower",
                        )
                        self.assertCountEqual(
                            [str(a) for a in ret[2]],
                            [str(a) for a in program.fast_preprocessing[1]],
                            "upper",
                        )
                        self.assertCountEqual(
                            ret[1], program.fast_preprocessing[0], "lower"
                        )
                        self.assertCountEqual(
                            ret[2], program.fast_preprocessing[1], "upper"
                        )

    def test_generator(self):
        self.maxDiff = None
        for i, program in enumerate(programs):
            prg = program.ground_reification
            if prg is not None and program.has_fast_preprocessing:
                with self.subTest(
                    format_subtest_message(
                        i, program.program, program.candidates_02_str
                    )
                ):
                    ret = fast_preprocessing(prg)
                    if ret is None:
                        continue
                    candidates = generate_candidates(prg, ret)
                    candidate_str = [
                        (sorted(str(a) for a in c.pos), sorted(str(a) for a in c.neg))
                        for c in candidates
                    ]
                    expected_str = [
                        (sorted(str(a) for a in c.pos), sorted(str(a) for a in c.neg))
                        for c in program.candidates_02
                    ]
                    self.assertCountEqual(
                        candidate_str, expected_str, "candidates string"
                    )
                    candidate_with_assumption_str = [
                        (
                            sorted(str(a) for a in c.pos),
                            sorted(str(a) for a in c.neg),
                            sorted(str(a) for a in c.extra_assumptions.pos),
                            sorted(str(a) for a in c.extra_assumptions.neg),
                        )
                        for c in candidates
                    ]
                    expected_with_assumption_str = [
                        (
                            sorted(str(a) for a in c.pos),
                            sorted(str(a) for a in c.neg),
                            sorted(str(a) for a in c.extra_assumptions.pos),
                            sorted(str(a) for a in c.extra_assumptions.neg),
                        )
                        for c in program.candidates_02
                    ]
                    self.assertCountEqual(
                        candidate_with_assumption_str,
                        expected_with_assumption_str,
                        "with assumptions string",
                    )

                    for model in candidates:
                        model.pos.sort()
                        model.neg.sort()
                        model.extra_assumptions.pos.sort()
                        model.extra_assumptions.neg.sort()
                    for model in program.candidates_02:
                        model.pos.sort()
                        model.neg.sort()
                        model.extra_assumptions.pos.sort()
                        model.extra_assumptions.neg.sort()
                    self.assertCountEqual(candidates, program.candidates_02)
