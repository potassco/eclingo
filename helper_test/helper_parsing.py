import unittest

import clingo as _clingo

from eclingo.util import clingoext as _clingoext
from eclingo.util.logger import silent_logger
from eclingo.util.astutil import ast_repr as _ast_repr

from eclingo.parsing import parse_program as _parse_program
from eclingo.internal_states import ShowStatement

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
        self.eclingo_semantics = "c19-1"

    def parse_program(self, stm, parameters=(), name="base"):
        ret = []
        _parse_program(stm, ret.append, parameters, name, semantics=self.eclingo_semantics)
        return _flatten(ret)

    def clingo_parse_program(self, stm):
        ret = []
        _clingo.parse_program(stm, ret.append)
        return ret

    def assert_equal_parsing_program(self, program, expected_program):
        parsed_program = self.parse_program(program)
        self.__assert_equal_parsing_program(parsed_program, expected_program)

    def __assert_equal_parsing_program(self, parsed_program, expected_program):
        expected_program = self.clingo_parse_program(expected_program)
        if self.printing:
            print("--- program ---")
            print(parsed_program)
            if self.printing_ast_repr:
                print(_ast_repr(parsed_program))
            print("--- expected program ---")
            if self.printing_ast_repr:
                print(expected_program)
                print(_ast_repr(expected_program))
        self.assert_equal_ordered(parsed_program, expected_program)

    def assert_equal_parsing_program_with_show(self, program, expected_program, expected_show):
        parsed_program = self.parse_program(program)
        program_without_show = []
        show_statements = []
        for statement in parsed_program:
            if isinstance(statement, ShowStatement):
                show_statements.append(statement)
            else:
                program_without_show.append(statement)
        self.__assert_equal_parsing_program(program_without_show, expected_program)
        self.assert_equal_ordered(show_statements, expected_show)