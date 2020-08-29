

from pprint import pprint
from eclingo.solver.world_view_builder import WorldWiewBuilderWithShow
from helper_test.helper_eclingo import EclingoTestHelper

class WorldWiewBuilderWithShowTestHelper(EclingoTestHelper):

    def assert_equal_show_program(self, program, expected_show_program):
        self.eclingo_control = self._control_and_ground(program)
        wv_builder = WorldWiewBuilderWithShow(self.eclingo_control.control)
        ground_program = wv_builder.control.ground_program.pretty()
        if self.printing:
            print("\n--- program ---")
            pprint(ground_program)
        ground_program = sorted(map(str, ground_program.as_list()))
        self.assert_equal_ordered(ground_program, expected_show_program)