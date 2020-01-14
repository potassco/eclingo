import clingo


def _show_result(k_list):
    result = []
    for atom in k_list:
        aux_name = 'aux_'

        if not atom.positive:
            aux_name += 'sn_'

        result.append(clingo.Function(aux_name+atom.name, atom.arguments, True))

    return result


def solve(candidates_gen, candidates_test, epistemic_atoms, show_signatures, models):
    model_count = 0
    with candidates_gen.solve(yield_=True) as candidates_gen_handle:
        for model in candidates_gen_handle:
            k_lits = set()
            k_not_lits = set()
            not_k_lits = set()
            not_k_not_lits = set()
            for epistemic in epistemic_atoms:
                if epistemic in model.symbols(shown=True):
                    if 'aux_not_' in epistemic.name:
                        k_not_lits.add(epistemic)
                    else:
                        k_lits.add(epistemic)
                else:
                    if 'aux_not_' in epistemic.name:
                        not_k_not_lits.add(epistemic)
                    else:
                        not_k_lits.add(epistemic)
            assumptions = [(atom, True) for atom in k_lits | k_not_lits] + \
                          [(atom, False) for atom in not_k_lits | not_k_not_lits]
            test = True
            if k_lits | not_k_lits:
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

            if test and (k_not_lits | not_k_not_lits):
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
                if show_signatures:
                    show_atoms = []
                    for (name, arity, positive) in show_signatures:
                        show_atoms += [atom.symbol for atom in
                                       candidates_gen.symbolic_atoms.by_signature(
                                           name, arity, positive)]

                    candidates_test.configuration.solve.enum_mode = 'cautious'
                    with candidates_test.solve(yield_=True, assumptions=assumptions) \
                            as candidates_test_handle:
                        *_, cautious_model = candidates_test_handle
                        k_atoms = [atom for atom in show_atoms
                                   if atom in cautious_model.symbols(atoms=True)]

                    yield _show_result(k_atoms)

                else:
                    yield model.symbols(shown=True)

                if model_count == models:
                    break
