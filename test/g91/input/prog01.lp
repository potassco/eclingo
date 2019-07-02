p, q.
r :- p.
r :- q.
s :- &k{ r }.
t :- not &k{ ~ p }.
u :- t, &k{ ~ q }.
