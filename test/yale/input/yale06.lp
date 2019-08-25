%%%%%%%  fluents   %%%%%%%%%
inertial(loaded).
inertial(alive).
inertial(wounded).
inertial(aimed).

%%%%%%%  actions   %%%%%%%%
action(load).
action(pull_trigger).
action(aim).

%%%%%%  executable  %%%%%%% 
executable(pull_trigger,T):-  stepless(T).
executable(load,T) :- -holds(loaded,T),stepless(T).
executable(aim,T):-  stepless(T).

%%%%%  effects   %%%%%%%
holds(aimed, T+1) :- occurs(aim, T), stepless(T).
-holds(aimed,T+1) :- occurs(load, T), stepless(T).
-holds(aimed, T+1) :- occurs(pull_trigger,T), stepless(T).

holds(wounded,T+1):- occurs(pull_trigger,T), holds(loaded,T), -holds(wounded,T), holds(alive,T), holds(aimed,T),stepless(T).
-holds(alive,T+1):-occurs(pull_trigger,T),holds(loaded,T), holds(wounded,T), holds(aimed,T), stepless(T).
-holds(loaded,T+1):-occurs(pull_trigger,T),stepless(T).
holds(loaded,T+1):-occurs(load,T),stepless(T).

%%%% initial state %%%%%
holds(alive,0).
{holds(loaded,0)}.
-holds(wounded,0).
{holds(aimed,0)}.