class Parser:

    def __init__(self, candidates_gen, candidates_test, predicates, optimization):
        self._candidates_gen = candidates_gen
        self._candidates_test = candidates_test
        self._predicates = predicates
        self._optimization = optimization
        self.epistemic_atoms = {}

    def parse(self):
        _add_grounding_rules(predicates, [candidates_gen, candidates_test])

        candidates_gen.ground([('base', [])])
        candidates_test.ground([('base', [])])

        k_signatures = [(name, arity, positive)
                        for (name, arity, positive) in candidates_gen.symbolic_atoms.signatures
                        if 'aux_' in name]

        epistemic_atoms = {}
        for control_object in [candidates_gen, candidates_test]:
            with control_object.backend() as backend:
                for (name, arity, positive) in k_signatures:
                    for atom in candidates_gen.symbolic_atoms.by_signature(name, arity, positive):
                        backend.add_rule([atom.literal], [], True)

                        epistemic_symbol = atom.symbol
                        name = epistemic_symbol.name.replace('aux_', '')
                        positive = True
                        if 'sn_' in epistemic_symbol.name:
                            name = name.replace('sn_', '')
                            positive = False
                        if 'not_' in epistemic_symbol.name:
                            name = name.replace('not_', '')
                        epistemic_atoms.update(
                            {epistemic_symbol: clingo.Function(name, epistemic_symbol.arguments,
                                                            positive)})

            control_object.cleanup()

        candidates_gen.add('projection', [], _generate_projection_directives(k_signatures))
        candidates_gen.ground([('projection', [])])

        if optimization > 0:
            with candidates_gen.backend() as backend:
                for epistemic, atom in epistemic_atoms.items():
                    atom_lit = backend.add_atom(atom)
                    if 'not_' not in epistemic.name:
                        atom_lit = 0-atom_lit
                    backend.add_rule([], [backend.add_atom(epistemic), atom_lit], False)
