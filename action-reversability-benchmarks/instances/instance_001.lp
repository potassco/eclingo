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

contains(X, value(X, B)) :- variable(X), boolean(B).

% actions
action(action("del-all")).
precondition(action("del-all"), variable("f0"), value(variable("f0"), true)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f0"), value(variable("f0"), false)) :- action(action("del-all")).

action(action("add-f0")).
postcondition(action("add-f0"), effect(unconditional), variable("f0"), value(variable("f0"), true)) :- action(action("add-f0")).

horizon(1).
