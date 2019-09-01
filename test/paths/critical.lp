%%% Find edges that are always used
critical(X,Y) :- &k{in(X,Y)}, edge(X,Y).
#show critical/2.

%%% Find edges that are never used
irrelevant(X,Y) :- &k{~ in(X,Y)}, edge(X,Y).
#show irrelevant/2.
