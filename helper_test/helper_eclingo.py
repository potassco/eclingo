from eclingo import config as _config
from eclingo import control as _control
from eclingo.internal_states import internal_control

from . import helper


class EclingoTestHelper(helper.TestHelper):
    def setUp(self):
        super().setUp()
        self.eclingo_control = None

    def _control_and_ground(self, program):
        control = internal_control.InternalStateControl(message_limit=0)
        config = _config.AppConfig()
        config.eclingo_semantics = "c19-1"
        eclingo_control = _control.Control(control=control, config=config)
        eclingo_control.add_program(program)
        eclingo_control.ground()
        return eclingo_control

    def control_solve(self, program):
        control = internal_control.InternalStateControl(message_limit=0)
        config = _config.AppConfig()
        config.eclingo_semantics = "c19-1"
        control.configuration.solve.project = "auto,3"
        control.configuration.solve.models = 0

        eclingo_control = _control.Control(control, config)
        eclingo_control.add_program(program)

        wviews = []
        for world_view in eclingo_control.solve():
            world_view = sorted(str(symbol) for symbol in world_view.symbols)
            wviews.append(world_view)

        return sorted(wviews)

    def assert_equal_world_views(self, program, expected):
        wviews = self.control_solve(program)
        self.assertEqual(wviews, sorted(sorted(wv) for wv in expected))
