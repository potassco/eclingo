import clingo
from eclingo.parser.observer import WFMObserver


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

        if self._optimization > 2:
            self._approximate_wfm()
        else:
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
                    body.append(f'{body_literal.name}({body_literal_arguments})')
                else:
                    body.append(body_literal.name)
            body.append(external)
            body_string = (', ').join(body)

            if epistemic_term.arguments:
                epistemic_arguments = (', ').join([str(argument)
                                                   for argument in epistemic_term.arguments])
                rules.append(f'{epistemic_term.name}({epistemic_arguments}) \
                    :- {negative}{term}({epistemic_arguments}), {body_string}.')
            else:
                rules.append(f'{epistemic_term.name} :- {negative}{term}, {body_string}.')

        for control_object in [self._candidates_gen, self._candidates_test]:
            control_object.add('base', [], f'#external {external}.')
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
            projection_directives += f'#project {name}/{arity}.\n'
            projection_directives += f'#show {name}/{arity}.\n'
        self._candidates_gen.add('projection', [], projection_directives)
        self._candidates_gen.ground([('projection', [])])

    def _optimization1(self):
        with self._candidates_gen.backend() as backend:
            for epistemic, atom in self.epistemic_atoms.items():
                atom_lit = backend.add_atom(atom)
                if 'not_' not in epistemic.name:
                    atom_lit = 0-atom_lit
                backend.add_rule([], [backend.add_atom(epistemic), atom_lit], False)

    def _approximate_wfm(self):
        observer = WFMObserver()
        self._candidates_gen.register_observer(observer, False)
        visited = []
        test = True
        while test:
            self._candidates_gen.ground([('base', [])])

            externals = {atom.literal for atom in self._candidates_gen.symbolic_atoms
                         if atom.is_external}
            symbolic_atoms = {atom.literal: str(atom.symbol)
                              for atom in self._candidates_gen.symbolic_atoms}
            affected_atoms = {symbol.replace('aux_', '').replace('not_', '').replace('sn_', '-')
                              for symbol in symbolic_atoms.values()
                              if 'aux_' in symbol}

            facts = {symbolic_atoms.get(fact) for fact in observer.get_facts()}
            heads = {symbolic_atoms.get(head) for head in observer.get_heads(externals)}

            found = []
            for fact in facts:
                if fact not in visited:
                    aux_atom = 'aux_'
                    aux_atom += fact.replace('-', 'sn_')
                    found.append(f'{aux_atom}.')
                    visited.append(fact)
                    visited.append(aux_atom)
            for atom in affected_atoms:
                if atom not in visited and atom not in heads:
                    aux_atom = 'aux_not_'
                    aux_atom += atom.replace('-', 'sn_')
                    found.append(f'{aux_atom}.')
                    visited.append(atom)
                    visited.append(aux_atom)

            if found:
                self._candidates_gen.add('base', [], "%s" % ("\n").join(found))
                observer.reset_facts()
                observer.reset_heads()
            else:
                test = False
                del observer
