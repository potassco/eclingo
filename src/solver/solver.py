def solve(candidates_gen, candidates_test, epistemic_atoms, models):
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
            assumptions = [(atom, True) for atom in (k_lits | k_not_lits)] + \
                          [(atom, False) for atom in (not_k_lits | not_k_not_lits)]
            test = True
            if (k_lits | not_k_lits):
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
                yield model.symbols(shown=True)

                if model_count == models:
                    break
