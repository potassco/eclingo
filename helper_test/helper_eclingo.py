import eclingo as _eclingo

from eclingo.util import clingoext as _clingoext
from eclingo.util.logger import silent_logger
from eclingo.util.astutil import ast_repr as _ast_repr

from eclingo.parsing import parse_program as _parse_program
from eclingo.internal_states import ShowStatement

from . import helper

class EclingoTestHelper(helper.TestHelper):

    def setUp(self):
        super().setUp()
        self.eclingo_control = None
    
    def _control_and_ground(self, program):
        control  = _eclingo.internal_states.InternalStateControl(message_limit=0)
        config   = _eclingo.config.AppConfig()
        config.eclingo_semantics = "c19-1"
        eclingo_control = _eclingo.control.Control(control=control, config=config)
        eclingo_control.add_program(program)
        eclingo_control.ground()
        return eclingo_control

    def solve(self, program):
        self.eclingo_control = self._control_and_ground(program)
        return self.eclingo_control.solve()

    def assert_equal_world_views(self, world_views, expected):
        sorted_world_views = []
        for world_view in world_views:
            world_view = sorted(str(symbol) for symbol in world_view.symbols)
            sorted_world_views.append(world_view)
        sorted_world_views = sorted(sorted_world_views)
        self.assertEqual(sorted_world_views, sorted(sorted(wv) for wv in expected))

    def assert_equal_show_symbols(self, program, expected_show_symbols):
        self.eclingo_control = self._control_and_ground(program)
        self.assertEqual(sorted(str(symbolic_atom.symbol) for symbolic_atom in self.eclingo_control.control.show_symbolic_atoms()), sorted(expected_show_symbols))