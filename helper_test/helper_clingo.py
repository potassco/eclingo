from eclingo.util import clingoext as _clingoext
from eclingo.util.logger import silent_logger
from . import helper



class ClingoTestHelper(helper.TestHelper):

    # def __init__(self):
    #     self.printing = False
    #     self.clingo_control: _clingoext.Control = None
    #     self.program_added = False

    def setUp(self):
        super().setUp()
        self.clingo_control = _clingoext.Control(logger=silent_logger)
        self.program_added = False

    def add_program(self, program):
        self.clingo_control.add_program(program)
        self.program_added = True

    def assert_equal_clingo_parsed_program(self, program, expected):
        self.add_program(program)
        result = self.clingo_control.parsed_program
        self._print_ast(result)
        self.assert_equal_ordered(result, expected)

    def assert_equal_clingo_ground_program(self, program, expected):
        if not self.program_added:
            self.add_program(program)
        self.clingo_control.ground([("base", [])])
        result = self.clingo_control.ground_program
        self._print(result)
        self.assert_equal_ordered(result, expected)


