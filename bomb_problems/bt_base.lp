%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% arguments %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% input: input_length(L).
% input: num_packages(NPL).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% problem description %%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

step(0..L) :- max_length(L).
stepless(0..L-1) :- max_length(L).

%%%%% occurs  %%%%%%%
occurs(A,S) :- action(A), stepless(S), not &k{ ~ occurs(A,S) }.
bot :- occurs(A,S), not executable(A,S).
:- { occurs(A,S) } > 1, stepless(S).

%%%%% goal  %%%%%%%
goal :- -holds(unsafe, LEN), not bot, max_length(LEN).

:- not &k{ goal }.

%%%%% defaults and inertia  %%%%%%%
-holds(F,0)   :- not  holds(F,0), fluent(F).
 holds(F,S+1) :- fluent(F), inertial(F), stepless(S),  holds(F,S), not  -holds(F,S+1).
-holds(F,S+1) :- fluent(F), inertial(F), stepless(S), -holds(F,S), not   holds(F,S+1).
