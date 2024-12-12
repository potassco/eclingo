"""
Main module providing the application logic.
"""

import sys
import time
from typing import Final, Sequence

from clingo import Flag
from clingo.application import clingo_main

from eclingo.config import AppConfig
from eclingo.control import Control

from . import __version__

STATISTICS_FIRST_FIELD_SIZE: Final[int] = 14


def statistics(eclingo_control: Control, time: float):  # pragma: no cover
    assert eclingo_control.solver is not None
    if int(eclingo_control.control.configuration.stats) > 0:
        sys.stderr.write("\n")  # pragma: no cover
        sys.stderr.write(
            f"{'Time ':<{STATISTICS_FIRST_FIELD_SIZE}}: {time:.3f}s "
            f"(Solving: {eclingo_control.solving_time:.3f}s"
            f"   Grounding: {eclingo_control.grounding_time:.3f}s"
            f"   Preprocessing: {eclingo_control.solver.preprocessing_time:.3f}s)\n"
            f"{' '*(STATISTICS_FIRST_FIELD_SIZE+11)}"
            f"Main grounding time              : {eclingo_control.main_grounding_time:.3f}s\n"
            f"{' '*(STATISTICS_FIRST_FIELD_SIZE+11)}"
            f"Generator grounding time         : {eclingo_control.solver.generator_grounding_time:.3f}s\n"
            f"{' '*(STATISTICS_FIRST_FIELD_SIZE+11)}"
            f"Tester grounding time            : {eclingo_control.solver.tester_grounding_time:.3f}s\n"
            f"{' '*(STATISTICS_FIRST_FIELD_SIZE+11)}"
            f"Worldview builder grounding time : {eclingo_control.solver.world_wivew_builder_grounding_time:.3f}s\n"
        )
        sys.stderr.write(
            f"{'Candidates':<{STATISTICS_FIRST_FIELD_SIZE}}: {eclingo_control.solver.number_of_candidates()}\n"
        )
        sys.stderr.write(
            f"{'Tester calls':<{STATISTICS_FIRST_FIELD_SIZE}}: {eclingo_control.solver.number_of_tester_calls()}\n"
        )


class Application:
    """
    Application class that can be used with `clingo.clingo_main` to solve CSP
    problems.
    """

    def __init__(self):
        self.program_name = "eclingo"
        self.version = __version__
        self.config = AppConfig()
        self.ingnore_shows = Flag()
        self.use_preprocessing = Flag(True)
        self.use_propagate = Flag(True)

    def _parse_string(self, config, attr):
        def parse(value):
            setattr(config, attr, value)  # pragma: no cover
            return True  # pragma: no cover

        return parse

    def _parse_int(self, config, attr):
        def parse(value):
            setattr(config, attr, int(value))  # pragma: no cover
            return True  # pragma: no cover

        return parse

    def register_options(self, options) -> None:
        """
        Register eclingo related options.
        """
        group = "Eclingo Options"

        options.add(
            group=group,
            option="semantics",
            description="Sets eclingo to use an specified semantics",
            parser=self._parse_string(self.config, "eclingo_semantics"),
            argument="<ELP_semantics>",
        )

        options.add(
            group=group,
            option="output-e",
            description="Rewrites the program using reification",
            parser=self._parse_string(self.config, "eclingo_rewritten"),
            argument="<rewritten>",
        )

        options.add(
            group=group,
            option="preprocessing-level",
            description="Sets the preprocessing-level\n" "      0: No preprocessing",
            parser=self._parse_int(self.config, "preprocessing_level"),
            argument="<l>",
        )

        options.add_flag(
            group=group,
            option="ignore-shows",
            description="Show statements are ignored (Default false)",
            target=self.ingnore_shows,
        )

        options.add_flag(
            group=group,
            option="eclingo-propagate",
            description="Uses the propagation inside of the generator (Default true)",
            target=self.use_propagate,
        )

    def _read(self, path):
        if path == "-":
            return sys.stdin.read()
        with open(path) as file_:
            return file_.read()

    def main(self, control: Control, files: Sequence[str]) -> None:
        """
        Entry point of the application registering the propagator and
        implementing the standard ground and solve functionality.
        """
        start_time = time.time()

        if not files:
            files = ["-"]

        eclingo_control = Control(control, self.config)

        for path in files:
            eclingo_control.add_program(self._read(path))

        if self.config.eclingo_rewritten == "rewritten":
            for stm in eclingo_control.rewritten_program[1:]:
                sys.stdout.write(str(stm))
                sys.stdout.write("\n")
            return
        self.config.ignore_shows = self.ingnore_shows.flag
        self.config.propagate = self.use_propagate.flag

        eclingo_control.ground()

        # Command check
        try:
            output_index = sys.argv.index("--output=")
        except ValueError:
            output_index = -1
        if (
            "--output=reify" in sys.argv
            or (output_index >= 0 and sys.argv[output_index + 1] == "reify")
            or "--text" in sys.argv
        ):
            return  # pragma: no cover

        eclingo_control.preprocess()
        eclingo_control.prepare_solver()

        sys.stdout.write("Solving...\n")
        wv_number = 0
        for wv_number, world_view in enumerate(eclingo_control.solve(), 1):
            sys.stdout.write("World view: %d\n" % wv_number)
            sys.stdout.write(str(world_view))
            sys.stdout.write("\n")
        if wv_number >= 1:
            sys.stdout.write("SATISFIABLE\n")
        else:
            sys.stdout.write("UNSATISFIABLE\n")
        end_time = time.time()
        total_time = end_time - start_time
        statistics(eclingo_control, total_time)


def secondary_main(argv):
    sys.argv.append("--outf=3")
    application = Application()
    result = clingo_main(application, argv[1:])
    return int(result)


def main():
    return secondary_main(sys.argv)
