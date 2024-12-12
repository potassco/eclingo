% p :- &k{ p }.
p :- &k{ p }, p.
p , not p :- &k{ p }.
% s :- &k{ p }.
s , not s :- &k{ p }.
s :- &k{ p }, p.
p , q.
:- not s.
