%#const horizon=1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Horizon, must be defined externally
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
time(0).
time(T+1) :- time(T), T<=H, horizon(H).

%%%%%%%% guess action to check for reversability %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%chosen(A) | -chosen(A) :- action(action(A)).
 chosen(A) :- action(action(A)), not &k{-chosen(A)}.
-chosen(A) :- action(action(A)), not &k{ chosen(A)}.

:- chosen(A), chosen(B), A!=B.
onechosen :- chosen(A).
:- not onechosen.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Establish initial state
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

holds(V, Val, 0) :- chosen(A), precondition(action(A), variable(V), value(variable(V), Val)).
relevant(V) :- holds(V, Val, 0).

%holds(V,Val,0) | -holds(V,Val,0) :- variable(variable(V)), contains(variable(V),value(variable(V),Val)).
%oneholds(V,0) :- holds(V,Val,0).
%:- variable(variable(V)), not oneholds(V,0).
%:- holds(V,Val,0), holds(V,Val1,0), Val != Val1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Perform actions
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

 occurs(A, 1) :- chosen(A).
 occurs(A, T) :- action(action(A)), time(T), T > 1, not &k{-occurs(A, T)}.
-occurs(A, T) :- action(action(A)), time(T), T > 1, not &k{ occurs(A, T)}.

:- occurs(A,T), occurs(B,T), A!=B.
oneoccurs(T) :- occurs(A,T), time(T), T > 0.
:- time(T), T>0, not oneoccurs(T).
plan(A, T-1) :- occurs(A, T), T > 1.

%occurs(A,T) :- action(A), time(T), not &k{ ~ occurs(A,T)}.


% Check preconditions
:- occurs(A, T), precondition(action(A), variable(V), value(variable(V), Val)), not holds(V, Val, T - 1).

% check that action doesn't touch fluents outside precondition of the checked action
:- occurs(A, T), precondition(action(A), variable(V), value(variable(V), Val)), not relevant(V).
:- occurs(A, T), postcondition(action(A), effect(unconditional), variable(V), value(variable(V), Val)), not relevant(V).

% Apply effects
caused(V, Val, T) :-
	occurs(A, T),
	postcondition(action(A), E, variable(V), value(variable(V), Val)).

%	holds(VPre, ValPre, T - 1) : precondition(action(A), variable(VPre), value(variable(VPre), ValPre)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Inertia rules
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

modified(V, T) :- caused(V, _, T).

holds(V, Val, T) :- caused(V, Val, T).
holds(V, Val, T) :- holds(V, Val, T - 1), not modified(V, T), time(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Verify that goal is met (i.e. we return to the origin state)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

noreversal :- holds(V, Val, 0), not holds(V, Val, H+1), horizon(H).
noreversal :- holds(V, Val, H+1), not holds(V, Val, 0), horizon(H).

% noreversal should not hold in any belief set
:- not &k{ ~ noreversal}.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show chosen/1.
#show plan/2.
