p, q.
r :- p.
r :- q.
s :- &k{ r }.
t :- not &k{ not p }.
u :- t, &k{ not q }.
