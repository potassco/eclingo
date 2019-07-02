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


def load_program(program, read_dict, backend):
    write_dict = {}
    new_program = []
    for (head, body, choice) in program:
        new_program_head = []
        new_program_body = []
        for term in head:
            term, neg = check_neg(term)
            literal, write_dict = \
                add_atom(term, read_dict, write_dict, backend)
            if neg:
                new_program_head.append(0-literal)
            else:
                new_program_head.append(literal)
        for term in body:
            term, neg = check_neg(term)
            literal, write_dict = \
                add_atom(term, read_dict, write_dict, backend)
            if neg:
                new_program_body.append(0-literal)
            else:
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
    models = []
    with control.solve(yield_=True) as handle:
        for model in handle:
            models.append(model.symbols(atoms=True))

    return models
