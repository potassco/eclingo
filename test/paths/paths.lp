%%% Find linear route from start to goal

reach(X) :- start(X).
reach(Y) :- reach(X), in(X,Y).
1 {in(X,Y): edge(X,Y) } 1 :- reach(X), not goal(X).

:- goal(X), not reach(X).

vtx(X) :- edge(X,_).
vtx(Y) :- edge(_,Y).

#show in/2.


