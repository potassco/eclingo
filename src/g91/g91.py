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


def get_literal(term, read_dict, backend):
    term, neg = check_neg(term)
    symbol = read_dict.get(term)
    literal = backend.add_atom(symbol)
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
                argument = \
                    resolve_theory_term(term_argument, dictionary, backend)
                arguments.append(argument)
        symbol = clingo.Function(term.name, arguments)
        literal = backend.add_atom(symbol)
        dictionary.update({literal: symbol})

    return symbol


def load_program(program, read_dict, backend):
    for (head, body, choice) in program:
        new_program_head = []
        new_program_body = []
        for term in head:
            literal = \
                get_literal(term, read_dict, backend)
            new_program_head.append(literal)
        for term in body:
            literal = \
                get_literal(term, read_dict, backend)
            new_program_body.append(literal)
        backend.add_rule(new_program_head, new_program_body, choice)


def append_epistemic_constraints(epistemic_atoms, backend):
    for epistemic, atom in epistemic_atoms.items():
        epistemic_literal = backend.add_atom(epistemic)
        atom_literal = backend.add_atom(atom)
        if 'aux_not_' not in epistemic.name:
            atom_literal = 0 - atom_literal
        backend.add_rule([], [epistemic_literal, atom_literal], False)


def generate_projection_directives(epistemic_atoms):
    string = ''
    for atom in epistemic_atoms:
        string = string + ('#project %s/%d.\n' % (atom.name, len(atom.arguments)))
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
                positive = True
                if epistemic_term.name == '~':
                    epistemic_term = epistemic_term.arguments[0]
                    aux = aux+'not_'
                if epistemic_term.name == '-':
                    epistemic_term = epistemic_term.arguments[0]
                    aux = aux+'sn_'
                    positive = False
                epistemic_term = \
                    resolve_theory_term(epistemic_term, symbolic_pi_atoms, backend)
                epistemic_symbol = clingo.Function(aux+epistemic_term.name,
                                                   epistemic_term.arguments)
                epistemic_literal = backend.add_atom(epistemic_symbol)
                symbol = clingo.Function(epistemic_term.name, epistemic_term.arguments, positive)
                literal = backend.add_atom(symbol)
                epistemic_atoms.update({epistemic_symbol: symbol})
                symbolic_pi_atoms.update({epistemic_literal: epistemic_symbol, literal: symbol})
                pi_aux.append(([epistemic_literal], [], True))
                term = epistemic_literal
            if neg:
                pi_aux_body.append(0-term)
            else:
                pi_aux_body.append(term)
        pi_aux.append((head, pi_aux_body, choice))

    return pi_aux, epistemic_atoms


def process(models, input_files):
    parser = clingo.Control()
    parser.load(THEORY_PATH)
    for input_file in input_files:
        parser.load(input_file)

    observer = Observer()
    parser.register_observer(observer, False)
    parser.ground([('base', [])])

    symbolic_pi_atoms = {x.literal: x.symbol for x in parser.symbolic_atoms}
    theory_pi_atoms = {x.literal: x.elements[0].terms[0] for x in parser.theory_atoms}

    with parser.backend() as backend:
        (pi_aux, epistemic_atoms) = \
            build_pi_aux(observer.rules, symbolic_pi_atoms, theory_pi_atoms, backend)

    candidates_test = clingo.Control(['0'])
    with candidates_test.backend() as backend:
        load_program(pi_aux, symbolic_pi_atoms, backend)

    candidates_gen = clingo.Control(['0', '--project'])
    with candidates_gen.backend() as backend:
        load_program(pi_aux, symbolic_pi_atoms, backend)
        append_epistemic_constraints(epistemic_atoms, backend)

    candidates_gen.add('base', [], generate_projection_directives(epistemic_atoms))
    candidates_gen.ground([('base', [])])
    model_count = 0
    with candidates_gen.solve(yield_=True) as candidates_gen_handle:
        for model in candidates_gen_handle:
            k_lits = []
            k_not_lits = []
            not_k_lits = []
            not_k_not_lits = []
            for epistemic in epistemic_atoms:
                if epistemic in model.symbols(shown=True):
                    if 'aux_not_' in epistemic.name:
                        k_not_lits.append(epistemic)
                    else:
                        k_lits.append(epistemic)
                else:
                    if 'aux_not_' in epistemic.name:
                        not_k_not_lits.append(epistemic)
                    else:
                        not_k_lits.append(epistemic)
            assumptions = [(atom, True) for atom in k_lits+k_not_lits] + \
                          [(atom, False) for atom in not_k_lits+not_k_not_lits]
            test = True
            if k_lits+not_k_lits:
                candidates_test.configuration.solve.enum_mode = 'cautious'
                with candidates_test.solve(yield_=True, assumptions=assumptions) \
                        as candidates_test_handle:
                    for cautious_model in candidates_test_handle:
                        for epistemic in k_lits:
                            atom = epistemic_atoms.get(epistemic)
                            if atom not in cautious_model.symbols(atoms=True):
                                test = False
                                break
                    if test:
                        for epistemic in not_k_lits:
                            atom = epistemic_atoms.get(epistemic)
                            if atom in cautious_model.symbols(atoms=True):
                                test = False
                                break

            if test and (k_not_lits+not_k_not_lits):
                candidates_test.configuration.solve.enum_mode = 'brave'
                with candidates_test.solve(yield_=True, assumptions=assumptions) \
                        as candidates_test_handle:
                    for brave_model in candidates_test_handle:
                        for epistemic in k_not_lits:
                            atom = epistemic_atoms.get(epistemic)
                            if atom in brave_model.symbols(atoms=True):
                                test = False
                                break
                    if test:
                        for epistemic in not_k_not_lits:
                            atom = epistemic_atoms.get(epistemic)
                            if atom not in brave_model.symbols(atoms=True):
                                test = False
                                break

            if test:
                model_count += 1
                yield model.symbols(shown=True)

                if model_count == models:
                    break
