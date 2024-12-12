import clingo
import clingox.program


def parse_program(program_str: str):
    control = clingo.Control()
    program = clingox.program.Program()
    control.register_observer(clingox.program.ProgramObserver(program))
    control.add(program_str)
    control.ground()
    return [f.symbol for f in program.facts]


# if __name__ == "__main__":
# control = clingo.Control()
# program = parse_program("a(1). b(1).")
# print(program)
# with control.backend() as backend:
#     mapping = clingox.program.Remapping(backend, program.output_atoms, program.facts)
#     program.add_to_backend(backend, mapping)
# control.add("c(X) :- a(X).")
# control.ground()
# with control.solve(yield_=True) as handle:
#     print("=========")
#     for model in handle:
#         print(model)

# with control.builder() as builder:
