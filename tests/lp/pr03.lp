a(X) :- &k{ not b(X)}, dom(X).
a(X) :- &k{ b(X)}, &k{ c(X)}.
{ b(1) }.
b(2).
c(1).
dom(1..3).
d(X) :- &k{ not not b(X)}, dom(X).
