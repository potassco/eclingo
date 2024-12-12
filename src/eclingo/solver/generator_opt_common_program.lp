symbolic_atom(SA) :- atom_map(SA, _).

symbolic_epistemic_atom(k(A)) :- symbolic_atom(k(A)).
symbolic_objective_atom(OSA)  :- symbolic_atom(OSA), not symbolic_epistemic_atom(OSA).

epistemic_atom_map(KSA, KA) :- atom_map(KSA, KA), symbolic_epistemic_atom(KSA).
objective_atom_map(OSA, OA) :- atom_map(OSA, OA), symbolic_objective_atom(OSA).

epistemic_atom_int(KA) :- epistemic_atom_map(_, KA).
objective_atom_int(A)  :- objective_atom_map(_, A).

epistemic_map(KA,OA) :- epistemic_atom_map(KSA, KA), objective_atom_map(OSA, OA), KSA = k(OSA).