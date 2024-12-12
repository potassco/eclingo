auxfalse :- false, not auxfalse.holds_alive_0.
holds_loaded_0.
false :- &k{occurs_pull_trigger_0}, &k{occurs_load_0}.
false :- &k{occurs_load_0}, &k{occurs_pull_trigger_0}.
occurs_0 :- &k{occurs_load_0}.
occurs_0 :- &k{occurs_pull_trigger_0}.
false :- not occurs_0.
occurs_load_0 :- not &k{ not occurs_load_0}.
occurs_pull_trigger_0 :- not &k{ not occurs_pull_trigger_0}.
ggoal :- &k{goal}.
false :- not ggoal.
executable_pull_trigger_0.
nholds_loaded_1 :- occurs_pull_trigger_0.
holds_loaded_1 :- occurs_load_0.
holds_loaded_1 :- not nholds_loaded_1.
holds_alive_1 :- not nholds_alive_1.
nholds_alive_1 :- occurs_pull_trigger_0.
imposs :- occurs_load_0.
goal :- not imposs, nholds_alive_1.
false :- occurs_load_0, occurs_pull_trigger_0.
false :- occurs_pull_trigger_0, occurs_load_0.
false :- nholds_loaded_1, holds_loaded_1.
false :- nholds_alive_1, holds_alive_1.
