from unittest import TestCase

import clingo
from clingox.testing.ast import ASTTestCase

from eclingo import util
from eclingo.config import AppConfig
from eclingo.control import Control

# python -m unittest tests.test_util.TestRewritten


class TestCase(ASTTestCase):
    def assert_equal_program_rewritten(self, program, expected):
        control = clingo.Control(message_limit=0)
        config = AppConfig(eclingo_rewritten="rewritten")
        eclingo_control = Control(control, config)
        eclingo_control.add_program(program)

        parsed_prg = []
        for i in range(1, len(eclingo_control.rewritten_program)):
            parsed_prg.append(str(eclingo_control.rewritten_program[i]))
        self.assertListEqual(parsed_prg, expected)


class TestPartition(TestCase):
    def test_size_1(self):
        self.assertEqual(
            util.partition(list(x for x in range(1, 10)), lambda x: x % 2 == 0),
            ([2, 4, 6, 8], [1, 3, 5, 7, 9]),
        )

    def test_size_2(self):
        self.assertEqual(
            util.partition(
                list(x for x in range(1, 10)),
                lambda x: x % 2 == 0,
                lambda x: x % 5 == 0,
            ),
            ([2, 4, 6, 8], [5], [1, 3, 7, 9]),
        )

    def test_size_3(self):
        self.assertEqual(
            util.partition(
                list(x for x in range(1, 10)),
                lambda x: x % 2 == 0,
                lambda x: x % 5 == 0,
                lambda x: x % 7 == 0,
            ),
            ([2, 4, 6, 8], [5], [7], [1, 3, 9]),
        )

    def test_size_4(self):
        self.assertEqual(
            util.partition(
                list(x for x in range(1, 10)),
                lambda x: x % 2 == 0,
                lambda x: x % 5 == 0,
                lambda x: x % 7 == 0,
                lambda x: x % 9 == 0,
            ),
            ([2, 4, 6, 8], [5], [7], [9], [1, 3]),
        )

    def test_size_more(self):
        self.assertEqual(
            util.partition(
                list(x for x in range(1, 14)),
                lambda x: x % 2 == 0,
                lambda x: x % 7 == 0,
                lambda x: x % 9 == 0,
                lambda x: x % 11 == 0,
                lambda x: x % 13 == 0,
            ),
            ([2, 4, 6, 8, 10, 12], [7], [9], [11], [13], [1, 3, 5]),
        )


class TestRewritten(TestCase):
    def test_rewritten(self):
        self.assert_equal_program_rewritten(
            "a. b :- &k{a}.", ["u(a).", "u(b) :- k(u(a)).", "{ k(u(a)) } :- u(a)."]
        )
