% a :- &k{ a }.
a :- &k{ a }, a.
a , not  a :- &k{ a }.
{a}.
:- not aux.
aux :- &k{ a }, a.
aux , not aux :- &k{ a }.
