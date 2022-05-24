"""
Main module providing the application logic.
"""

import sys
from typing import Sequence

from eclingo.config import AppConfig
from eclingo.control import Control
from eclingo.control import __version__
from eclingo.internal_states import internal_control
from eclingo.internal_states.internal_control import InternalStateControl

_FALSE = ["0", "no", "false"]
_TRUE = ["1", "yes", "true"]





class Application(internal_control.Application):
    """
    Application class that can be used with `clingo.clingo_main` to solve CSP
    problems.
    """

    def __init__(self):
        self.program_name = "eclingo"
        self.version = __version__
        self.config = AppConfig()

    def _parse_int(self, config, attr, min_value=None, max_value=None):
        """
        Parse integer and store result in `config.attr`.

        Here `attr` has to be the name of an attribute. Optionally, a minimum
        and maximum value can be given for the integer.
        """
        def parse(value):
            num = int(value)
            if min_value is not None and num < min_value:
                return False
            if max_value is not None and num > max_value:
                return False
            setattr(config, attr, num)
            return True
        return parse


    def register_options(self, options):
        """
        Register eclingo related options.
        """
        group = "Eclingo Options"

        options.add(
            group, "eclingo-verbose",
            "Set verbosity level of eclingo to <n>", self._parse_int(self.config, "eclingo_verbose"), argument="<n>")

    def _read(self, path):
        if path == "-":
            return sys.stdin.read()
        with open(path) as file_:
            return file_.read()

    def main(self, control: InternalStateControl, files: Sequence[str]) -> None:
        """
        Entry point of the application registering the propagator and
        implementing the standard ground and solve functionality.
        """
        if not files:
            files = ["-"]


        eclingo_control = Control(control, self.config)

        for path in files:
            eclingo_control.add_program(self._read(path))

        eclingo_control.ground()
        eclingo_control.preprocess()
        eclingo_control.prepare_solver()

        sys.stdout.write('Solving...\n')
        wv_number = 1
        for world_view in eclingo_control.solve():
            sys.stdout.write('World view: %d\n' % wv_number)
            sys.stdout.write(str(world_view))
            sys.stdout.write('\n')
            wv_number += 1
        if wv_number > 1:
            sys.stdout.write('SATISFIABLE\n')
        else:
            sys.stdout.write('UNSATISFIABLE\n')


def main():
    sys.argv.append('--outf=3')
    application = Application()
    result = internal_control.clingo_main(application, sys.argv[1:])
    sys.exit(int(result))

if __name__ == '__main__':
    main()
