import clingo

THEORY_PATH = 'asp/theory/theory.lp'


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

    return literal


def get_literal(term, read_dict, write_dict, backend):
    term, neg = check_neg(term)
    literal = \
        add_atom(term, read_dict, write_dict, backend)
    if neg:
        literal = (0-literal)

    return literal


def resolve_theory_term(term, dictionary, backend):
    if term.type == clingo.TheoryTermType.Number:
        symbol = clingo.Number(term.number)
    else:
        arguments = []
        if term.arguments:
            for term_argument in term.arguments:
                argument, dictionary = \
                    resolve_theory_term(term_argument, dictionary, backend)
                arguments.append(argument)
        symbol = clingo.Function(term.name, arguments)
        literal = backend.add_atom(symbol)
        dictionary.update({literal: symbol})

    return symbol, dictionary


def add_constraint(epistemic, symbolic_atom, write_dict, backend):
    new_literal = backend.add_atom(symbolic_atom)
    write_dict.update({new_literal: symbolic_atom})
    if 'aux_not' in epistemic.name:
        new_literal = 0-new_literal
    backend.add_rule([], [new_literal], False)


def load_program(program, read_dict, backend):
    write_dict = {}
    for (head, body, choice) in program:
        new_program_head = []
        new_program_body = []
        for term in head:
            literal = \
                get_literal(term, read_dict, write_dict, backend)
            new_program_head.append(literal)
        for term in body:
            literal = \
                get_literal(term, read_dict, write_dict, backend)
            new_program_body.append(literal)
        backend.add_rule(new_program_head, new_program_body, choice)

    return write_dict


def append_epistemic_rules(epistemic_atoms, symbolic_pi_atoms, backend):
    for epistemic, atom in epistemic_atoms.items():
        epistemic_literal = backend.add_atom(epistemic)
        atom_literal = backend.add_atom(atom)
        symbolic_pi_atoms.update({epistemic_literal: epistemic, atom_literal: atom})
        backend.add_rule([epistemic_literal], [], True)
        if 'aux_not_' not in epistemic.name:
            atom_literal = 0 - atom_literal
        backend.add_rule([], [epistemic_literal, atom_literal], False)


def generate_show_directives(epistemic_atoms):
    string = ''
    for atom in epistemic_atoms:
        string = string + ('#show %s/%d.\n' % (atom.name, len(atom.arguments)))

    return string


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
                epistemic_term, symbolic_pi_atoms = \
                    resolve_theory_term(epistemic_term, symbolic_pi_atoms, backend)
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

    return pi_aux, epistemic_atoms


def build_pi_m(pi_aux, symbolic_pi_aux_atoms, epistemic_atoms, candidates, backend):
    symbolic_pi_m_atoms = {}
    pi_m = []
    for (head, body, choice) in pi_aux:
        pi_head = []
        pi_body = []
        in_candidates = True
        for term in head:
            literal = \
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
    parser = clingo.Control()
    parser.load(THEORY_PATH)
    parser.load(input_program)

    observer = Observer()
    parser.register_observer(observer, False)
    parser.ground([('base', [])])

    symbolic_pi_atoms = {x.literal: x.symbol for x in parser.symbolic_atoms}
    theory_pi_atoms = {x.literal: x.elements[0].terms[0] for x in parser.theory_atoms}

    with parser.backend() as backend:
        (pi_aux, epistemic_atoms) = \
            build_pi_aux(observer.rules, symbolic_pi_atoms, theory_pi_atoms, backend)


    candidates_gen = clingo.Control(['0', '--project'])
    with candidates_gen.backend() as backend:
        symbolic_pi_aux_atoms = \
            load_program(pi_aux, symbolic_pi_atoms, backend)
        append_epistemic_rules(epistemic_atoms, symbolic_pi_aux_atoms, backend)
        
    candidates_gen.add('base', [], generate_show_directives(epistemic_atoms))
    candidates_gen.ground([('base', [])])
    with candidates_gen.solve(yield_=True) as handle:
        candidates = {frozenset([symbol for symbol in model.symbols(shown=True)])
                      for model in handle}


    world_views = set()
    for world_view in candidates:
        with candidates_gen.backend() as backend:
            (pi_m, symbolic_pi_m_atoms) = \
                build_pi_m(pi_aux, symbolic_pi_atoms,
                           epistemic_atoms, world_view, backend)

        failed = False
        for epistemic, symbolic in epistemic_atoms.items():
            candidates_test = clingo.Control()
            with candidates_test.backend() as backend:
                pi_m_atoms = \
                    load_program(pi_m, symbolic_pi_m_atoms, backend)
                add_constraint(epistemic, symbolic, pi_m_atoms, backend)

            test_result = candidates_test.solve()
            if (epistemic in world_view) and (test_result.satisfiable):
                failed = True
                break
            elif (epistemic not in world_view) and (test_result.unsatisfiable):
                failed = True
                break
        if not failed:
            world_views.add(world_view)

    return world_views
