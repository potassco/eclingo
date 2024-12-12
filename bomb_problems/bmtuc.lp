%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% arguments %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% input: input_length(L).
% input: input_toilet(T).
num_packages(L/2) :- input_length(L).
max_length(L-1)   :- input_length(L).
toilet(1..T)      :- input_toilets(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% initial states %%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

package(1..NP) :- num_packages(NP).

{ holds(armed(P),0) } :- package(P).
:- not 1 { holds(armed(P),0) : package(P) } 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% problem description %%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%  fluents   %%%%%%%%%%%%%%%%%%

fluent(armed(P))   :- package(P).
inertial(armed(P)) :- package(P).

fluent(dunked(P))   :- package(P).
inertial(dunked(P)) :- package(P).

fluent(clogged).
inertial(clogged).

fluent(unsafe).

%%%%%%%  actions   %%%%%%%%
action(dunk(P,L)) :- package(P), toilet(L).
action(flush(L))  :- toilet(L).

%%%%%%  executable  %%%%%%%
executable(dunk(P,L), S) :- action(dunk(P,L)), toilet(L), not holds(clogged(L),S), step(S).

executable(flush(L), S)  :- action(flush(L)), toilet(L), step(S).

%%%%%  direct effects   %%%%%%%
-holds(armed(P),  T+1)  :- occurs(dunk(P,L), T), step(T).
 holds(dunked(P), T+1)  :- occurs(dunk(P,L), T), step(T).
 holds(clogged(L), T+1) :- occurs(dunk(P,L), T), toilet(L), step(T).

-holds(clogged(L), T+1) :- occurs(flush(L), T), toilet(L), step(T).

%%%%%  indirect effects   %%%%%%%
 holds(unsafe, T) :- holds(armed(P),   T), step(T).
-holds(unsafe, T) :- not holds(unsafe, T), step(T).
