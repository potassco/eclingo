%%%%%%%  fluents   %%%%%%%%%
inertial(loaded).
inertial(alive).
inertial(wounded).
inertial(aimed).
inertial(cocked).

%%%%%%%  actions   %%%%%%%%
action(load).
action(fire).
action(aim).
action(cock).

%%%%%%  executable  %%%%%%%
executable(fire,T):-  holds(cocked,T), stepless(T).
executable(load,T) :- -holds(loaded,T),stepless(T).
executable(aim,T):-  stepless(T).
executable(cock,T) :- -holds(cocked,T),stepless(T).


%%%%%  effects   %%%%%%%
holds(aimed, T+1) :- occurs(aim, T), stepless(T).
-holds(aimed,T+1) :- occurs(cock, T), stepless(T).
-holds(aimed,T+1) :- occurs(load, T), stepless(T).
-holds(aimed, T+1) :- occurs(fire,T), stepless(T).

holds(cocked, T+1) :- occurs(cock, T), stepless(T).
-holds(cocked, T+1) :- occurs(fire,T), stepless(T).

holds(wounded,T+1):- occurs(fire,T), holds(loaded,T),
                     -holds(wounded,T), holds(alive,T),
                     holds(aimed,T), holds(cocked,T), stepless(T).
-holds(alive,T+1):- occurs(fire,T),holds(loaded,T),
                    holds(wounded,T), holds(alive,T),
                    holds(aimed,T), holds(cocked,T), stepless(T).
-holds(loaded,T+1):-occurs(fire,T),stepless(T).
holds(loaded,T+1):-occurs(load,T),stepless(T).


%%%% initial state %%%%%
{holds(alive,0)}.
{holds(loaded,0)}.
{holds(wounded,0)}.
{holds(aimed,0)}.
-holds(cocked,0).
