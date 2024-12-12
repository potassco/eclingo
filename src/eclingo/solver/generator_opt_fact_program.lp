% Propagate facts into epistemic facts

:- fact(OSA), epistemic_atom_map(k(OSA), KA), not hold(KA).
positive_extra_assumptions(OSA) :- fact(OSA), symbolic_epistemic_atom(k(OSA)).
#show positive_extra_assumptions/1.