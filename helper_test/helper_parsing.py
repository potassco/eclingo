import clingo.ast as _ast

from eclingo.config import AppConfig
from eclingo.parsing.parser import parse_program as _parse_program

from . import helper


def _flatten(lst):
    result = []
    for lst2 in lst:
        if isinstance(lst2, list):
            for e in lst2:
                result.append(e)
        else:
            result.append(lst2)
    return result


class ParsingTestHelper(helper.TestHelper):
    def setUp(self):
        super().setUp()
        self.config: AppConfig = AppConfig(semantics="c19-1")

    def parse_program(self, stm, parameters=(), name="base"):
        ret = []
        _parse_program(stm, ret.append, parameters, name, config=self.config)
        return _flatten(ret)

    def clingo_parse_program(self, stm):
        ret = []
        _ast.parse_string(stm, ret.append)
        return ret

    def assert_equal_parsing_program(self, program, expected_program):
        parsed_program = self.parse_program(program)
        self.__assert_equal_parsing_program(parsed_program, expected_program)

    def __assert_equal_parsing_program(self, parsed_program, expected_program):
        expected_program = self.clingo_parse_program(expected_program)
        parsed_program.sort()
        expected_program.sort()
        self.assertEqual(len(parsed_program), len(expected_program))
        for r1, r2 in zip(parsed_program, expected_program):
            self.assertEqual(str(r1), str(r2))
            self.assertEqual(r1, r2)
        self.assertCountEqual(
            [str(s) for s in parsed_program], [str(s) for s in expected_program]
        )
        self.assertCountEqual(parsed_program, expected_program)
        self.assert_equal_ordered(parsed_program, expected_program)

    def assert_equal_parsing_program_with_show(
        self, program, expected_program, expected_show
    ):
        parsed_program = self.parse_program(program)
        program_without_show = []
        show_statements = []
        for statement in parsed_program:
            # if isinstance(statement, ShowStatement):
            #     show_statements.append(statement)
            # else:
            #     program_without_show.append(statement)
            program_without_show.append(statement)
        self.__assert_equal_parsing_program(program_without_show, expected_program)
        self.assert_equal_ordered(show_statements, expected_show)
