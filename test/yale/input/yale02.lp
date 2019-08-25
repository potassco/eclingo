%%%%%%%  fluents   %%%%%%%%%
inertial(loaded).
inertial(alive).

%%%%%%%  actions   %%%%%%%%
action(load).
action(pull_trigger).

%%%%%%  executable  %%%%%%% 
executable(pull_trigger,T):-  stepless(T).
executable(load,T) :- -holds(loaded,T),stepless(T).

%%%%%  effects   %%%%%%%
-holds(alive,T+1):-occurs(pull_trigger,T),holds(loaded,T),stepless(T).
-holds(loaded,T+1):-occurs(pull_trigger,T),stepless(T).
holds(loaded,T+1):-occurs(load,T),stepless(T).

%%%% initial state %%%%%
holds(alive,0).
-holds(loaded,0).