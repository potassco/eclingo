%---------------------------------------
% domain
%---------------------------------------

% utils
boolean(true).
boolean(false).

% types
type(type("object")).

% variables
variable(variable("f0")).
variable(variable("f1")).
variable(variable("f2")).
variable(variable("f3")).
variable(variable("f4")).
variable(variable("f5")).
variable(variable("f6")).
variable(variable("f7")).
variable(variable("f8")).
variable(variable("f9")).
variable(variable("f10")).

contains(X, value(X, B)) :- variable(X), boolean(B).

% actions
action(action("del-all")).
precondition(action("del-all"), variable("f0"), value(variable("f0"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f1"), value(variable("f1"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f2"), value(variable("f2"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f3"), value(variable("f3"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f4"), value(variable("f4"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f5"), value(variable("f5"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f6"), value(variable("f6"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f7"), value(variable("f7"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f8"), value(variable("f8"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f9"), value(variable("f9"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f10"), value(variable("f10"), true)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f0"), value(variable("f0"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f1"), value(variable("f1"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f2"), value(variable("f2"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f3"), value(variable("f3"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f4"), value(variable("f4"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f5"), value(variable("f5"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f6"), value(variable("f6"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f7"), value(variable("f7"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f8"), value(variable("f8"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f9"), value(variable("f9"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f10"), value(variable("f10"), false)) :- action(action("del-all")).

action(action("add-f0")).
postcondition(action("add-f0"), effect(unconditional), variable("f0"), value(variable("f0"), true)) :- action(action("add-f0")).

action(action("add-f1")).
precondition(action("add-f1"), variable("f0"), value(variable("f0"), true)) :- action(action("add-f1")).
postcondition(action("add-f1"), effect(unconditional), variable("f1"), value(variable("f1"), true)) :- action(action("add-f1")).

action(action("add-f2")).
precondition(action("add-f2"), variable("f1"), value(variable("f1"), true)) :- action(action("add-f2")).
postcondition(action("add-f2"), effect(unconditional), variable("f2"), value(variable("f2"), true)) :- action(action("add-f2")).

action(action("add-f3")).
precondition(action("add-f3"), variable("f2"), value(variable("f2"), true)) :- action(action("add-f3")).
postcondition(action("add-f3"), effect(unconditional), variable("f3"), value(variable("f3"), true)) :- action(action("add-f3")).

action(action("add-f4")).
precondition(action("add-f4"), variable("f3"), value(variable("f3"), true)) :- action(action("add-f4")).
postcondition(action("add-f4"), effect(unconditional), variable("f4"), value(variable("f4"), true)) :- action(action("add-f4")).

action(action("add-f5")).
precondition(action("add-f5"), variable("f4"), value(variable("f4"), true)) :- action(action("add-f5")).
postcondition(action("add-f5"), effect(unconditional), variable("f5"), value(variable("f5"), true)) :- action(action("add-f5")).

action(action("add-f6")).
precondition(action("add-f6"), variable("f5"), value(variable("f5"), true)) :- action(action("add-f6")).
postcondition(action("add-f6"), effect(unconditional), variable("f6"), value(variable("f6"), true)) :- action(action("add-f6")).

action(action("add-f7")).
precondition(action("add-f7"), variable("f6"), value(variable("f6"), true)) :- action(action("add-f7")).
postcondition(action("add-f7"), effect(unconditional), variable("f7"), value(variable("f7"), true)) :- action(action("add-f7")).

action(action("add-f8")).
precondition(action("add-f8"), variable("f7"), value(variable("f7"), true)) :- action(action("add-f8")).
postcondition(action("add-f8"), effect(unconditional), variable("f8"), value(variable("f8"), true)) :- action(action("add-f8")).

action(action("add-f9")).
precondition(action("add-f9"), variable("f8"), value(variable("f8"), true)) :- action(action("add-f9")).
postcondition(action("add-f9"), effect(unconditional), variable("f9"), value(variable("f9"), true)) :- action(action("add-f9")).

action(action("add-f10")).
precondition(action("add-f10"), variable("f9"), value(variable("f9"), true)) :- action(action("add-f10")).
postcondition(action("add-f10"), effect(unconditional), variable("f10"), value(variable("f10"), true)) :- action(action("add-f10")).

horizon(11).
