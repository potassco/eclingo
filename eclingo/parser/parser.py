import clingo

class Parser:

    def __init__(self, candidates_gen, candidates_test, predicates, optimization):
        self._candidates_gen = candidates_gen
        self._candidates_test = candidates_test
        self._predicates = predicates
        self._optimization = optimization
        self.epistemic_atoms = {}
        self.k_signatures = set()

    def parse(self):
        self._add_grounding_rules()

        self._candidates_gen.ground([('base', [])])
        self._candidates_test.ground([('base', [])])

        self.k_signatures.update({(literal.atom.term.name, len(literal.atom.term.arguments), True)
                                  for literal, _ in self._predicates})

        self._add_choice_rules()
        self._remove_grounding_rules()

        self._add_projection_directives()

        if self._optimization > 0:
            self._optimization1()

    def _add_grounding_rules(self):
        rules = []
        external = '_atom_to_be_released'

        for (predicate, positive_body) in self._predicates:
            epistemic_term = predicate.atom.term
            term = epistemic_term.name.replace('aux_', '')
            negative = ''
            if 'not_' in term:
                term = term.replace('not_', '')
                negative = 'not '
            if 'sn_' in term:
                term = term.replace('sn_', '-')

            body = []
            for body_literal in positive_body:
                body_literal = body_literal.atom.term
                if body_literal.arguments:
                    body_literal_arguments = (', ').join([str(argument)
                                                          for argument in body_literal.arguments])
                    body.append('{name}({arguments})'.format(name=body_literal.name,
                                                             arguments=body_literal_arguments))
                else:
                    body.append(body_literal.name)
            body.append(external)
            body_string = (', ').join(body)

            if epistemic_term.arguments:
                epistemic_arguments = (', ').join([str(argument)
                                                   for argument in epistemic_term.arguments])
                rules.append('{ep_term}({ep_args}) :- {negative}{term}({ep_args}), {body}.' \
                    .format(ep_term=epistemic_term.name, ep_args=epistemic_arguments,
                            negative=negative, term=term, body=body_string))
            else:
                rules.append('{epistemic_term} :- {negative}{term}, {body}.' \
                    .format(epistemic_term=epistemic_term.name, negative=negative,
                            term=term, body=body_string))

        for control_object in [self._candidates_gen, self._candidates_test]:
            control_object.add('base', [], '#external {}.'.format(external))
            control_object.add('base', [], '\n'.join(rules))

    def _add_choice_rules(self):
        with self._candidates_gen.backend() as gen_backend, \
            self._candidates_test.backend() as test_backend:
            for (name, arity, positive) in self.k_signatures:
                for atom in self._candidates_gen.symbolic_atoms \
                    .by_signature(name, arity, positive):
                    gen_backend.add_rule([atom.literal], [], True)
                    test_backend.add_rule([atom.literal], [], True)

                    epistemic_symbol = atom.symbol
                    name = epistemic_symbol.name.replace('aux_', '')
                    positive = True
                    if 'sn_' in epistemic_symbol.name:
                        name = name.replace('sn_', '')
                        positive = False
                    if 'not_' in epistemic_symbol.name:
                        name = name.replace('not_', '')
                    self.epistemic_atoms.update(
                        {epistemic_symbol: clingo.Function(name, epistemic_symbol.arguments,
                                                           positive)})

    def _remove_grounding_rules(self):
        self._candidates_gen.cleanup()
        self._candidates_test.cleanup()

    def _add_projection_directives(self):
        projection_directives = ''
        for (name, arity, _) in self.k_signatures:
            projection_directives += '#project {name}/{arity}.\n'.format(name=name, arity=arity)
            projection_directives += '#show {name}/{arity}.\n'.format(name=name, arity=arity)
        self._candidates_gen.add('projection', [], projection_directives)
        self._candidates_gen.ground([('projection', [])])

    def _optimization1(self):
        with self._candidates_gen.backend() as backend:
            for epistemic, atom in self.epistemic_atoms.items():
                atom_lit = backend.add_atom(atom)
                if 'not_' not in epistemic.name:
                    atom_lit = 0-atom_lit
                backend.add_rule([], [backend.add_atom(epistemic), atom_lit], False)
