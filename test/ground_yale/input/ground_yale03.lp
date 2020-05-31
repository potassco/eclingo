auxfalse :- false, not auxfalse.holds_alive_0.
false :- &k{occurs_pull_trigger_0}, &k{occurs_load_0}.
false :- &k{occurs_pull_trigger_1}, &k{occurs_load_1}.
false :- &k{occurs_pull_trigger_2}, &k{occurs_load_2}.
false :- &k{occurs_load_0}, &k{occurs_pull_trigger_0}.
false :- &k{occurs_load_1}, &k{occurs_pull_trigger_1}.
false :- &k{occurs_load_2}, &k{occurs_pull_trigger_2}.
occurs_0 :- &k{occurs_load_0}.
occurs_1 :- &k{occurs_load_1}.
occurs_2 :- &k{occurs_load_2}.
occurs_0 :- &k{occurs_pull_trigger_0}.
occurs_1 :- &k{occurs_pull_trigger_1}.
occurs_2 :- &k{occurs_pull_trigger_2}.
false :- not occurs_0.
false :- not occurs_1.
false :- not occurs_2.
occurs_load_0 :- not &k{~occurs_load_0}.
occurs_load_1 :- not &k{~occurs_load_1}.
occurs_load_2 :- not &k{~occurs_load_2}.
occurs_pull_trigger_0 :- not &k{~occurs_pull_trigger_0}.
occurs_pull_trigger_1 :- not &k{~occurs_pull_trigger_1}.
occurs_pull_trigger_2 :- not &k{~occurs_pull_trigger_2}.
ggoal :- &k{goal}.
false :- not ggoal.
executable_pull_trigger_0.
executable_pull_trigger_1.
executable_pull_trigger_2.
nholds_loaded_1 :- occurs_pull_trigger_0.
nholds_loaded_2 :- occurs_pull_trigger_1.
nholds_loaded_3 :- occurs_pull_trigger_2.
holds_loaded_1 :- occurs_load_0.
holds_loaded_2 :- occurs_load_1.
holds_loaded_3 :- occurs_load_2.
nholds_loaded_0 :- not holds_loaded_0.
holds_loaded_0 :- not nholds_loaded_0.
holds_loaded_1 :- holds_loaded_0, not nholds_loaded_1.
holds_loaded_3 :- holds_loaded_2, not nholds_loaded_3.
holds_loaded_2 :- holds_loaded_1, not nholds_loaded_2.
holds_alive_1 :- not nholds_alive_1.
holds_alive_2 :- holds_alive_1, not nholds_alive_2.
holds_alive_3 :- holds_alive_2, not nholds_alive_3.
nholds_alive_1 :- holds_loaded_0, occurs_pull_trigger_0.
nholds_alive_2 :- holds_loaded_1, occurs_pull_trigger_1.
nholds_alive_3 :- holds_loaded_2, occurs_pull_trigger_2.
nholds_loaded_0 :- not holds_loaded_0.
nholds_alive_3 :- nholds_alive_2, not holds_alive_3.
nholds_alive_2 :- nholds_alive_1, not holds_alive_2.
nholds_loaded_1 :- nholds_loaded_0, not holds_loaded_1.
nholds_loaded_3 :- nholds_loaded_2, not holds_loaded_3.
nholds_loaded_2 :- nholds_loaded_1, not holds_loaded_2.
executable_load_1 :- nholds_loaded_1.
executable_load_2 :- nholds_loaded_2.
executable_load_0 :- nholds_loaded_0.
imposs :- occurs_load_0, not executable_load_0.
imposs :- occurs_load_1, not executable_load_1.
imposs :- occurs_load_2, not executable_load_2.
goal :- not imposs, nholds_alive_3.
false :- occurs_load_0, occurs_pull_trigger_0.
false :- occurs_load_1, occurs_pull_trigger_1.
false :- occurs_load_2, occurs_pull_trigger_2.
false :- occurs_pull_trigger_0, occurs_load_0.
false :- occurs_pull_trigger_1, occurs_load_1.
false :- occurs_pull_trigger_2, occurs_load_2.
false :- nholds_loaded_1, holds_loaded_1.
false :- nholds_loaded_2, holds_loaded_2.
false :- nholds_loaded_3, holds_loaded_3.
false :- nholds_loaded_0, holds_loaded_0.
false :- nholds_alive_1, holds_alive_1.
false :- nholds_alive_2, holds_alive_2.
false :- nholds_alive_3, holds_alive_3.
