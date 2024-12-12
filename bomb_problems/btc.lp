%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% arguments %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% input: input_length(L).
num_packages(L/2) :- input_length(L).
max_length(L-1)   :- input_length(L).

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
action(dunk(P)) :- package(P).
action(flush).

%%%%%%  executable  %%%%%%%
executable(dunk(P), T) :- action(dunk(P)), -holds(clogged,T), step(T), not holds(dunked(P),T).

executable(flush,T) :- action(flush), step(T).

%%%%%  direct effects   %%%%%%%
-holds(armed(P),  T+1) :- occurs(dunk(P), T), step(T).
 holds(dunked(P), T+1) :- occurs(dunk(P), T), step(T).
 holds(clogged, T+1)   :- occurs(dunk(P), T), step(T).

-holds(clogged, T+1)   :- occurs(flush,   T), step(T).

%%%%%  indirect effects   %%%%%%%
 holds(unsafe, T) :- holds(armed(P),   T), step(T).
-holds(unsafe, T) :- not holds(unsafe, T), step(T).
