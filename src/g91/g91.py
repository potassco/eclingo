import clingo

THEORY_PATH = "asp/theory/theory.lp"


class Observer:
    def __init__(self):
        self.rules = []

    def rule(self, choice, head, body):
        self.rules.append((head, body, choice))


def check_neg(term):
    neg = False
    if term < 0:
        term = abs(term)
        neg = True

    return term, neg


def add_atom(term, read_dict, write_dict, backend):
    symbol = read_dict.get(term)
    literal = backend.add_atom(symbol)
    write_dict.update({literal: symbol})

    return literal, write_dict


def get_literal(term, read_dict, write_dict, backend):
    term, neg = check_neg(term)
    literal, write_dict = \
        add_atom(term, read_dict, write_dict, backend)
    if neg:
        literal = (0-literal)

    return literal, write_dict


def add_constraint(epistemic, symbolic_atom, program, write_dict, backend):
    new_literal = backend.add_atom(symbolic_atom)
    write_dict.update({new_literal: symbolic_atom})
    if 'aux_not' in epistemic.name:
        new_literal = 0-new_literal
    backend.add_rule([], [new_literal], False)
    program.append(([], [new_literal], False))

    return program, write_dict


def load_program(program, read_dict, backend):
    write_dict = {}
    new_program = []
    for (head, body, choice) in program:
        new_program_head = []
        new_program_body = []
        for term in head:
            literal, write_dict = \
                get_literal(term, read_dict, write_dict, backend)
            new_program_head.append(literal)
        for term in body:
            literal, write_dict = \
                get_literal(term, read_dict, write_dict, backend)
            new_program_body.append(literal)
        new_program.append((new_program_head, new_program_body, choice))
        backend.add_rule(new_program_head, new_program_body, choice)

    return new_program, write_dict


def build_pi_aux(rules, symbolic_pi_atoms, theory_pi_atoms, backend):
    epistemic_atoms = {}
    pi_aux = []
    for (head, body, choice) in rules:
        pi_aux_body = []
        for term in body:
            term, neg = check_neg(term)
            if symbolic_pi_atoms.get(term) is None:
                epistemic_term = theory_pi_atoms.get(term)
                aux = 'aux_'
                if epistemic_term.name == '~':
                    epistemic_term = epistemic_term.arguments[0]
                    aux = 'aux_not_'
                symbol = clingo.Function(aux+epistemic_term.name, epistemic_term.arguments)
                epistemic_atoms.update({symbol: clingo.Function(epistemic_term.name,
                                                                epistemic_term.arguments)})
                literal = backend.add_atom(symbol)
                symbolic_pi_atoms.update({literal: symbol})
                term = literal
            if neg:
                pi_aux_body.append(0-term)
            else:
                pi_aux_body.append(term)
        pi_aux.append((head, pi_aux_body, choice))
    for literal, symbol in symbolic_pi_atoms.items():
        if symbol in epistemic_atoms.keys():
            pi_aux.append(([literal], [], True))

    return pi_aux, symbolic_pi_atoms, epistemic_atoms


def build_pi_m(pi_aux, symbolic_pi_aux_atoms, epistemic_atoms, candidates, backend):
    symbolic_pi_m_atoms = {}
    pi_m = []
    for (head, body, choice) in pi_aux:
        if (not choice) and (head[0] not in epistemic_atoms.keys()):
            pi_head = []
            pi_body = []
            in_candidates = True
            for term in head:
                literal, symbolic_pi_m_atoms = \
                    get_literal(term, symbolic_pi_aux_atoms, symbolic_pi_m_atoms, backend)
                pi_head.append(literal)
            for term in body:
                term, neg = check_neg(term)
                symbol = symbolic_pi_aux_atoms.get(term)
                if symbol in epistemic_atoms.keys():
                    if ((symbol not in candidates) and
                            (not neg)) or ((symbol in candidates) and (neg)):
                        in_candidates = False
                        break
                else:
                    literal = backend.add_atom(symbol)
                    symbolic_pi_m_atoms.update({literal: symbol})
                    if neg:
                        pi_body.append(0-literal)
                    else:
                        pi_body.append(literal)
            if in_candidates:
                pi_m.append((pi_head, pi_body, choice))

    return pi_m, symbolic_pi_m_atoms


def process(input_program):
    observer = Observer()
    control = clingo.Control()
    control.load(THEORY_PATH)
    control.load(input_program)
    control.register_observer(observer, False)
    control.ground([("base", [])])

    pi = observer.rules
    symbolic_pi_atoms = {x.literal: x.symbol for x in control.symbolic_atoms}
    theory_pi_atoms = {x.literal: x.elements[0].terms[0] for x in control.theory_atoms}

    with control.backend() as backend:
        (pi_aux, symbolic_pi_atoms, epistemic_atoms) = \
            build_pi_aux(pi, symbolic_pi_atoms, theory_pi_atoms, backend)

    control = clingo.Control()
    with control.backend() as backend:
        (new_pi_aux, symbolic_pi_aux_atoms) = \
            load_program(pi_aux, symbolic_pi_atoms, backend)

    control.configuration.solve.models = 0
    with control.solve(yield_=True) as handle:
        candidates = {frozenset([symbol for symbol in model.symbols(atoms=True)
                                 if symbol in epistemic_atoms.keys()]) for model in handle}

    world_views = set()
    for world_view in candidates:
        with control.backend() as backend:
            pi_m, symbolic_pi_m_atoms = \
                 build_pi_m(new_pi_aux, symbolic_pi_aux_atoms,
                            epistemic_atoms, world_view, backend)

        failed = False
        for epistemic, symbolic in epistemic_atoms.items():
            control_m = clingo.Control()
            with control_m.backend() as backend:
                pi_m_program, pi_m_atoms = \
                    load_program(pi_m, symbolic_pi_m_atoms, backend)
                pi_m_program, pi_m_atoms = \
                    add_constraint(epistemic, symbolic, pi_m_program,
                                   pi_m_atoms, backend)

            test_result = control_m.solve()
            if (epistemic in world_view) and (test_result.satisfiable):
                failed = True
                break
            elif (epistemic not in world_view) and (test_result.unsatisfiable):
                failed = True
                break
        if not failed:
            world_views.add(world_view)

    return world_views
