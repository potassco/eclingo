stepless(0..length-1).

%%% Inertial fluents are fluents
fluent(F) :- inertial(F).

%%%% inertia %%%%
holds(F,S+1) :- inertial(F), stepless(S), holds(F,S),not  -holds(F,S+1).
-holds(F,S+1):- inertial(F), stepless(S),-holds(F,S),not   holds(F,S+1).

%%% non-concurrent actions
:- occurs(A,S), occurs(B,S), A!=B.

%%%% initial state: fluents false by default
-holds(F,0):-not  holds(F,0),fluent(F).

%%%%% goal  %%%%%%%
goal :- -holds(alive,length), not imposs.

%%%% epistemic %%%%%%%
imposs :- occurs(A,S), not executable(A,S).
:- not &k{goal}.

occurs(A,S) :- not &k{ ~ occurs(A,S) }, stepless(S), action(A).

occurs(S) :- &k{occurs(A,S)}, action(A), stepless(S).
:- not occurs(S), stepless(S).

:- &k{occurs(A,S)}, &k{occurs(B,S)}, action(A), action(B), stepless(S), A!=B.


%%%% show occurs/2 %%%%
#show occurs/2.