import unittest

import clingo
from clingox.program import Program, ProgramObserver, Remapping

from eclingo.solver.tester import CandidateTester


class TesterCase(unittest.TestCase):
    def assertEqualPrograms(self, expected_program, program):
        expected_program = [f"{s.strip()}." for s in program.split(".") if s]
        expected_program.sort()
        program = [s.strip() for s in str(program).split("\n")]
        program.sort()
        return self.assertListEqual(expected_program, program)

    def assertClingoxProgramAddToBackend(self, program):
        control_gen = clingo.control.Control()
        program1 = Program()
        control_gen.register_observer(ProgramObserver(program1))
        control_gen.add("base", [], program)
        control_gen.ground([("base", [])])
        self.assertEqualPrograms(program, str(program1))
        control_test = clingo.control.Control(["0"], message_limit=0)
        program2 = Program()
        control_test.register_observer(ProgramObserver(program2))
        with control_test.backend() as backend:
            mapping = Remapping(backend, program1.output_atoms, program1.facts)
            program1.add_to_backend(backend, mapping)
        self.assertEqualPrograms(program, str(program2))

    def assertInitControl(self, program):
        control_gen = clingo.Control()
        program1 = Program()
        control_gen.register_observer(ProgramObserver(program1))
        control_gen.add("base", [], program)
        control_gen.ground([("base", [])])
        self.assertEqualPrograms(program, str(program1))
        control_test = clingo.Control(["0"], message_limit=0)
        program2 = Program()
        control_test.register_observer(ProgramObserver(program2))
        CandidateTester._init_control_test(control_test, control_gen)
        self.assertEqualPrograms(program, str(program2))

    def test_clingox(self):
        self.assertClingoxProgramAddToBackend("{u_a}.")
        self.assertClingoxProgramAddToBackend("u_b :- k_a. {k_a}. {u_a}.")
        self.assertClingoxProgramAddToBackend(
            "u_a; u_b. u_c :- u_a. u_c :- u_b. u_d :- k_c. {k_c}."
        )

    def test_init_control(self):
        self.assertInitControl("{u_a}.")
        self.assertInitControl("u_b :- k_a. {k_a}. {u_a}.")
        self.assertInitControl("u_a; u_b. u_c :- u_a. u_c :- u_b. u_d :- k_c. {k_c}.")
