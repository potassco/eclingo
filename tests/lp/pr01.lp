a(X) :- not b, dom(X).
b :- not a(X), dom(X).
c.
d :- &k{ not not not not -a(X) ; b}, dom(X).
e :- &k{c}.

dom(1;2).
