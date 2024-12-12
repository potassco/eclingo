from pprint import pprint

from eclingo.solver.world_view_builder import WorldWiewBuilderReificationWithShow
from helper_test.helper_eclingo import EclingoTestHelper


class WorldWiewBuilderWithShowTestHelper(EclingoTestHelper):
    def assert_equal_show_program(self, program, expected_show_program):
        self.eclingo_control = self._control_and_ground(program)
        wv_builder = WorldWiewBuilderReificationWithShow(
            self.eclingo_control.grounder.reified_facts
        )
        facts = wv_builder.control.ground_program.facts
        shows = []
        for i in range(0, len(facts)):
            if facts[i].symbol.name == "output":
                if facts[i].symbol.arguments[0].name == "show_statement":
                    shows.append(facts[i].symbol.arguments[0])

        self.assert_equal_ordered(shows, expected_show_program)
