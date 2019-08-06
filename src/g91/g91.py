import clingo


def generate_projection_directives(k_signatures):
    string = ''
    for (name, arity, _) in k_signatures:
        string = string + ('#project %s/%d.\n' % (name, arity))
        string = string + ('#show %s/%d.\n' % (name, arity))

    return string


def add_grounding_rules(predicates, control_objects):
    rules = []
    external = '_atom_to_be_released'

    for predicate in predicates:
        epistemic_term = predicate.atom.term
        term = epistemic_term.name.replace('aux_', '') \
                                  .replace('not_', '').replace('sn_', '-')

        if epistemic_term.arguments:
            epistemic_arguments = []
            epistemic_arguments_counter = len(epistemic_term.arguments)

            for index in range(1, epistemic_arguments_counter+1):
                epistemic_arguments.append(('X%d' % index))
            epistemic_arguments = (', ').join(epistemic_arguments)
            rules.append('%s(%s) :- %s(%s), %s.' %
                         (epistemic_term.name, epistemic_arguments,
                          term, epistemic_arguments, external))
        else:
            rules.append('%s :- %s, %s.' % (epistemic_term.name, term, external))

    for control_object in control_objects:
        control_object.add('base', [], '#external %s.' % external)
        control_object.add('base', [], '\n'.join(rules))


def preprocess(ast, control_objects, predicates):
    if ast.type == clingo.ast.ASTType.Rule:
        preprocessed_body = []
        for body_literal in ast.body:
            if body_literal.atom.type == clingo.ast.ASTType.TheoryAtom:
                theory_term = body_literal.atom.elements[0].tuple[0]
                theory_element = theory_term.elements[0]
                symbol_name = 'aux_'
                for operator in theory_element.operators:
                    if operator == '~':
                        symbol_name += 'not_'
                    elif operator == '-':
                        symbol_name += 'sn_'
                if theory_element.term.type == clingo.ast.ASTType.Symbol:
                    symbol_name += theory_element.term.symbol.name
                    symbol_arguments = theory_element.term.symbol.arguments
                elif theory_element.term.type == clingo.ast.ASTType.TheoryFunction:
                    symbol_name += theory_element.term.name
                    symbol_arguments = [symbol_argument.elements[0].term
                                        for symbol_argument in theory_element.term.arguments]
                body_literal = clingo.ast.Literal(body_literal.location, body_literal.sign,
                                                  clingo.ast.SymbolicAtom(
                                                      clingo.ast.Function(body_literal.location,
                                                                          symbol_name,
                                                                          symbol_arguments, False)))
                preprocessed_body.append(body_literal)
                predicates.append(body_literal)
            else:
                preprocessed_body.append(body_literal)

        rule = clingo.ast.Rule(ast.location, ast.head, preprocessed_body)
        for control_object in control_objects:
            with control_object.builder() as builder:
                builder.add(rule)
    else:
        for control_object in control_objects:
            with control_object.builder() as builder:
                builder.add(ast)


def process(models, input_files):
    candidates_gen = clingo.Control(['0', '--project'])
    candidates_test = clingo.Control(['0'])

    predicates, epistemic_atoms = [], []
    for input_file in input_files:
        with open(input_file, 'r') as program:
            clingo.parse_program(program.read(),
                                 lambda ast: preprocess(ast, [candidates_gen, candidates_test],
                                                        predicates))
    add_grounding_rules(predicates, [candidates_gen, candidates_test])

    candidates_gen.ground([('base', [])])
    candidates_test.ground([('base', [])])

    k_signatures = [(name, arity, positive)
                    for (name, arity, positive) in candidates_gen.symbolic_atoms.signatures
                    if 'aux_' in name]

    epistemic_symbols = []
    for control_object in [candidates_gen, candidates_test]:
        with control_object.backend() as backend:
            for (name, arity, positive) in k_signatures:
                for atom in candidates_gen.symbolic_atoms.by_signature(name, arity):
                    epistemic_symbols.append(atom.symbol)
                    backend.add_rule([atom.literal], [], True)

        control_object.cleanup()

    epistemic_atoms = {}
    for symbol in epistemic_symbols:
        name = symbol.name.replace('aux_', '')
        positive = True
        if 'sn_' in symbol.name:
            name = name.replace('sn_', '')
            positive = False
        if 'not_' in symbol.name:
            name = name.replace('not_', '')

        epistemic_atoms.update({symbol: clingo.Function(name, symbol.arguments, positive)})

    candidates_gen.add('projection', [], generate_projection_directives(k_signatures))
    candidates_gen.ground([('projection', [])])

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
