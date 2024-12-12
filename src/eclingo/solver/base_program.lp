conjunction(B) :- literal_tuple(B), hold(L) : literal_tuple(B, L), L > 0;
                                not hold(L) : literal_tuple(B, -L), L > 0.

body(normal(B)) :- rule(_, normal(B)), conjunction (B).

body(sum(B, G)) :- rule (_, sum(B,G)),
                    #sum { W,L :     hold(L), weighted_literal_tuple(B,  L, W), L>0;
                           W,L : not hold(L), weighted_literal_tuple(B, -L, W), L>0} >= G.

hold(A) : atom_tuple(H,A) :- rule(disjunction(H), B), body(B).

{hold(A) : atom_tuple(H,A)} :- rule(choice(H), B), body(B).

fact(SA) :- output(SA, LT), #count {L : literal_tuple(LT, L)} = 0.

atom_map(SA, A) :- output(SA,LT), #count{LL : literal_tuple(LT, LL)} = 1, literal_tuple(LT, A).

hold_symbolic_atom(SA) :- atom_map(SA, A), hold(A).
hold_symbolic_atom(SA) :- fact(SA).
:- hold_symbolic_atom(u(-SA)), hold_symbolic_atom(u(SA)).

positive_candidate(k(A)) :- fact(k(A)).
positive_candidate(k(A)) :- output(k(A), B), conjunction(B).
negative_candidate(k(A)) :- output(k(A), B), not conjunction(B).

#show positive_candidate/1.
#show negative_candidate/1.

