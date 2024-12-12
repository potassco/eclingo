auxfalse :- false, not auxfalse.holds_alive_0.
holds_loaded_0.
nholds_wounded_0.
false :- &k{occurs_pull_trigger_0}, &k{occurs_load_0}.
false :- &k{occurs_aim_0}, &k{occurs_load_0}.
false :- &k{occurs_pull_trigger_1}, &k{occurs_load_1}.
false :- &k{occurs_aim_1}, &k{occurs_load_1}.
false :- &k{occurs_pull_trigger_2}, &k{occurs_load_2}.
false :- &k{occurs_aim_2}, &k{occurs_load_2}.
false :- &k{occurs_pull_trigger_3}, &k{occurs_load_3}.
false :- &k{occurs_aim_3}, &k{occurs_load_3}.
false :- &k{occurs_pull_trigger_4}, &k{occurs_load_4}.
false :- &k{occurs_aim_4}, &k{occurs_load_4}.
false :- &k{occurs_load_0}, &k{occurs_pull_trigger_0}.
false :- &k{occurs_aim_0}, &k{occurs_pull_trigger_0}.
false :- &k{occurs_load_1}, &k{occurs_pull_trigger_1}.
false :- &k{occurs_aim_1}, &k{occurs_pull_trigger_1}.
false :- &k{occurs_load_2}, &k{occurs_pull_trigger_2}.
false :- &k{occurs_aim_2}, &k{occurs_pull_trigger_2}.
false :- &k{occurs_load_3}, &k{occurs_pull_trigger_3}.
false :- &k{occurs_aim_3}, &k{occurs_pull_trigger_3}.
false :- &k{occurs_load_4}, &k{occurs_pull_trigger_4}.
false :- &k{occurs_aim_4}, &k{occurs_pull_trigger_4}.
false :- &k{occurs_load_0}, &k{occurs_aim_0}.
false :- &k{occurs_pull_trigger_0}, &k{occurs_aim_0}.
false :- &k{occurs_load_1}, &k{occurs_aim_1}.
false :- &k{occurs_pull_trigger_1}, &k{occurs_aim_1}.
false :- &k{occurs_load_2}, &k{occurs_aim_2}.
false :- &k{occurs_pull_trigger_2}, &k{occurs_aim_2}.
false :- &k{occurs_load_3}, &k{occurs_aim_3}.
false :- &k{occurs_pull_trigger_3}, &k{occurs_aim_3}.
false :- &k{occurs_load_4}, &k{occurs_aim_4}.
false :- &k{occurs_pull_trigger_4}, &k{occurs_aim_4}.
occurs_0 :- &k{occurs_load_0}.
occurs_1 :- &k{occurs_load_1}.
occurs_2 :- &k{occurs_load_2}.
occurs_3 :- &k{occurs_load_3}.
occurs_4 :- &k{occurs_load_4}.
occurs_0 :- &k{occurs_pull_trigger_0}.
occurs_1 :- &k{occurs_pull_trigger_1}.
occurs_2 :- &k{occurs_pull_trigger_2}.
occurs_3 :- &k{occurs_pull_trigger_3}.
occurs_4 :- &k{occurs_pull_trigger_4}.
occurs_0 :- &k{occurs_aim_0}.
occurs_1 :- &k{occurs_aim_1}.
occurs_2 :- &k{occurs_aim_2}.
occurs_3 :- &k{occurs_aim_3}.
occurs_4 :- &k{occurs_aim_4}.
false :- not occurs_0.
false :- not occurs_1.
false :- not occurs_2.
false :- not occurs_3.
false :- not occurs_4.
occurs_load_0 :- not &k{ not occurs_load_0}.
occurs_load_1 :- not &k{ not occurs_load_1}.
occurs_load_2 :- not &k{ not occurs_load_2}.
occurs_load_3 :- not &k{ not occurs_load_3}.
occurs_load_4 :- not &k{ not occurs_load_4}.
occurs_pull_trigger_0 :- not &k{ not occurs_pull_trigger_0}.
occurs_pull_trigger_1 :- not &k{ not occurs_pull_trigger_1}.
occurs_pull_trigger_2 :- not &k{ not occurs_pull_trigger_2}.
occurs_pull_trigger_3 :- not &k{ not occurs_pull_trigger_3}.
occurs_pull_trigger_4 :- not &k{ not occurs_pull_trigger_4}.
occurs_aim_0 :- not &k{ not occurs_aim_0}.
occurs_aim_1 :- not &k{ not occurs_aim_1}.
occurs_aim_2 :- not &k{ not occurs_aim_2}.
occurs_aim_3 :- not &k{ not occurs_aim_3}.
occurs_aim_4 :- not &k{ not occurs_aim_4}.
ggoal :- &k{goal}.
false :- not ggoal.
executable_pull_trigger_0.
executable_pull_trigger_1.
executable_pull_trigger_2.
executable_pull_trigger_3.
executable_pull_trigger_4.
nholds_loaded_1 :- occurs_pull_trigger_0.
nholds_loaded_2 :- occurs_pull_trigger_1.
nholds_loaded_3 :- occurs_pull_trigger_2.
nholds_loaded_4 :- occurs_pull_trigger_3.
nholds_loaded_5 :- occurs_pull_trigger_4.
nholds_aimed_1 :- occurs_load_0.
nholds_aimed_2 :- occurs_load_1.
nholds_aimed_3 :- occurs_load_2.
nholds_aimed_4 :- occurs_load_3.
nholds_aimed_5 :- occurs_load_4.
nholds_aimed_1 :- occurs_pull_trigger_0.
nholds_aimed_2 :- occurs_pull_trigger_1.
nholds_aimed_3 :- occurs_pull_trigger_2.
nholds_aimed_4 :- occurs_pull_trigger_3.
nholds_aimed_5 :- occurs_pull_trigger_4.
holds_aimed_1 :- occurs_aim_0.
holds_aimed_2 :- occurs_aim_1.
holds_aimed_3 :- occurs_aim_2.
holds_aimed_4 :- occurs_aim_3.
holds_aimed_5 :- occurs_aim_4.
holds_loaded_1 :- occurs_load_0.
holds_loaded_2 :- occurs_load_1.
holds_loaded_3 :- occurs_load_2.
holds_loaded_4 :- occurs_load_3.
holds_loaded_5 :- occurs_load_4.
holds_aimed_0 :- not nholds_aimed_0.
nholds_aimed_0 :- not holds_aimed_0.
nholds_aimed_0 :- not holds_aimed_0.
holds_wounded_1 :- holds_aimed_0, occurs_pull_trigger_0.
holds_aimed_1 :- holds_aimed_0, not nholds_aimed_1.
holds_loaded_5 :- holds_loaded_4, not nholds_loaded_5.
holds_loaded_4 :- holds_loaded_3, not nholds_loaded_4.
holds_loaded_3 :- holds_loaded_2, not nholds_loaded_3.
holds_loaded_2 :- holds_loaded_1, not nholds_loaded_2.
holds_aimed_5 :- holds_aimed_4, not nholds_aimed_5.
holds_aimed_4 :- holds_aimed_3, not nholds_aimed_4.
holds_aimed_3 :- holds_aimed_2, not nholds_aimed_3.
holds_aimed_2 :- holds_aimed_1, not nholds_aimed_2.
holds_loaded_1 :- not nholds_loaded_1.
holds_alive_1 :- not nholds_alive_1.
nholds_aimed_1 :- nholds_aimed_0, not holds_aimed_1.
nholds_aimed_5 :- nholds_aimed_4, not holds_aimed_5.
nholds_aimed_4 :- nholds_aimed_3, not holds_aimed_4.
nholds_aimed_3 :- nholds_aimed_2, not holds_aimed_3.
nholds_aimed_2 :- nholds_aimed_1, not holds_aimed_2.
nholds_loaded_5 :- nholds_loaded_4, not holds_loaded_5.
nholds_loaded_4 :- nholds_loaded_3, not holds_loaded_4.
nholds_loaded_3 :- nholds_loaded_2, not holds_loaded_3.
nholds_loaded_2 :- nholds_loaded_1, not holds_loaded_2.
nholds_wounded_1 :- not holds_wounded_1.
holds_alive_2 :- holds_alive_1, not nholds_alive_2.
holds_wounded_2 :- holds_wounded_1, not nholds_wounded_2.
nholds_alive_2 :- holds_aimed_1, holds_wounded_1, holds_loaded_1, occurs_pull_trigger_1.
holds_wounded_2 :- holds_aimed_1, holds_alive_1, nholds_wounded_1, holds_loaded_1, occurs_pull_trigger_1.
nholds_wounded_2 :- nholds_wounded_1, not holds_wounded_2.
holds_wounded_3 :- holds_aimed_2, holds_alive_2, nholds_wounded_2, holds_loaded_2, occurs_pull_trigger_2.
holds_wounded_3 :- holds_wounded_2, not nholds_wounded_3.
holds_alive_3 :- holds_alive_2, not nholds_alive_3.
nholds_alive_3 :- holds_aimed_2, holds_wounded_2, holds_loaded_2, occurs_pull_trigger_2.
nholds_wounded_3 :- nholds_wounded_2, not holds_wounded_3.
nholds_alive_3 :- nholds_alive_2, not holds_alive_3.
holds_alive_4 :- holds_alive_3, not nholds_alive_4.
holds_wounded_4 :- holds_wounded_3, not nholds_wounded_4.
nholds_alive_4 :- holds_aimed_3, holds_wounded_3, holds_loaded_3, occurs_pull_trigger_3.
holds_wounded_4 :- holds_aimed_3, holds_alive_3, nholds_wounded_3, holds_loaded_3, occurs_pull_trigger_3.
nholds_alive_4 :- nholds_alive_3, not holds_alive_4.
nholds_wounded_4 :- nholds_wounded_3, not holds_wounded_4.
holds_wounded_5 :- holds_aimed_4, holds_alive_4, nholds_wounded_4, holds_loaded_4, occurs_pull_trigger_4.
holds_wounded_5 :- holds_wounded_4, not nholds_wounded_5.
holds_alive_5 :- holds_alive_4, not nholds_alive_5.
nholds_alive_5 :- holds_aimed_4, holds_wounded_4, holds_loaded_4, occurs_pull_trigger_4.
nholds_wounded_5 :- nholds_wounded_4, not holds_wounded_5.
nholds_alive_5 :- nholds_alive_4, not holds_alive_5.
executable_load_1 :- nholds_loaded_1.
executable_load_2 :- nholds_loaded_2.
executable_load_3 :- nholds_loaded_3.
executable_load_4 :- nholds_loaded_4.
executable_aim_0.
executable_aim_1.
executable_aim_2.
executable_aim_3.
executable_aim_4.
imposs :- occurs_load_0.
imposs :- occurs_load_1, not executable_load_1.
imposs :- occurs_load_2, not executable_load_2.
imposs :- occurs_load_3, not executable_load_3.
imposs :- occurs_load_4, not executable_load_4.
goal :- not imposs, nholds_alive_5.
false :- occurs_load_0, occurs_pull_trigger_0.
false :- occurs_load_0, occurs_aim_0.
false :- occurs_load_1, occurs_pull_trigger_1.
false :- occurs_load_1, occurs_aim_1.
false :- occurs_load_2, occurs_pull_trigger_2.
false :- occurs_load_2, occurs_aim_2.
false :- occurs_load_3, occurs_pull_trigger_3.
false :- occurs_load_3, occurs_aim_3.
false :- occurs_load_4, occurs_pull_trigger_4.
false :- occurs_load_4, occurs_aim_4.
false :- occurs_pull_trigger_0, occurs_load_0.
false :- occurs_pull_trigger_0, occurs_aim_0.
false :- occurs_pull_trigger_1, occurs_load_1.
false :- occurs_pull_trigger_1, occurs_aim_1.
false :- occurs_pull_trigger_2, occurs_load_2.
false :- occurs_pull_trigger_2, occurs_aim_2.
false :- occurs_pull_trigger_3, occurs_load_3.
false :- occurs_pull_trigger_3, occurs_aim_3.
false :- occurs_pull_trigger_4, occurs_load_4.
false :- occurs_pull_trigger_4, occurs_aim_4.
false :- occurs_aim_0, occurs_load_0.
false :- occurs_aim_0, occurs_pull_trigger_0.
false :- occurs_aim_1, occurs_load_1.
false :- occurs_aim_1, occurs_pull_trigger_1.
false :- occurs_aim_2, occurs_load_2.
false :- occurs_aim_2, occurs_pull_trigger_2.
false :- occurs_aim_3, occurs_load_3.
false :- occurs_aim_3, occurs_pull_trigger_3.
false :- occurs_aim_4, occurs_load_4.
false :- occurs_aim_4, occurs_pull_trigger_4.
false :- nholds_loaded_1, holds_loaded_1.
false :- nholds_loaded_2, holds_loaded_2.
false :- nholds_loaded_3, holds_loaded_3.
false :- nholds_loaded_4, holds_loaded_4.
false :- nholds_loaded_5, holds_loaded_5.
false :- nholds_aimed_1, holds_aimed_1.
false :- nholds_aimed_2, holds_aimed_2.
false :- nholds_aimed_3, holds_aimed_3.
false :- nholds_aimed_4, holds_aimed_4.
false :- nholds_aimed_5, holds_aimed_5.
false :- nholds_aimed_0, holds_aimed_0.
false :- nholds_wounded_1, holds_wounded_1.
false :- nholds_alive_2, holds_alive_2.
false :- nholds_wounded_2, holds_wounded_2.
false :- nholds_wounded_3, holds_wounded_3.
false :- nholds_alive_3, holds_alive_3.
false :- nholds_alive_4, holds_alive_4.
false :- nholds_wounded_4, holds_wounded_4.
false :- nholds_wounded_5, holds_wounded_5.
false :- nholds_alive_5, holds_alive_5.
