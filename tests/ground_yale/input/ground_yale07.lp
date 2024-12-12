auxfalse :- false, not auxfalse.holds_alive_0.
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
false :- &k{occurs_pull_trigger_5}, &k{occurs_load_5}.
false :- &k{occurs_aim_5}, &k{occurs_load_5}.
false :- &k{occurs_pull_trigger_6}, &k{occurs_load_6}.
false :- &k{occurs_aim_6}, &k{occurs_load_6}.
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
false :- &k{occurs_load_5}, &k{occurs_pull_trigger_5}.
false :- &k{occurs_aim_5}, &k{occurs_pull_trigger_5}.
false :- &k{occurs_load_6}, &k{occurs_pull_trigger_6}.
false :- &k{occurs_aim_6}, &k{occurs_pull_trigger_6}.
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
false :- &k{occurs_load_5}, &k{occurs_aim_5}.
false :- &k{occurs_pull_trigger_5}, &k{occurs_aim_5}.
false :- &k{occurs_load_6}, &k{occurs_aim_6}.
false :- &k{occurs_pull_trigger_6}, &k{occurs_aim_6}.
occurs_0 :- &k{occurs_load_0}.
occurs_1 :- &k{occurs_load_1}.
occurs_2 :- &k{occurs_load_2}.
occurs_3 :- &k{occurs_load_3}.
occurs_4 :- &k{occurs_load_4}.
occurs_5 :- &k{occurs_load_5}.
occurs_6 :- &k{occurs_load_6}.
occurs_0 :- &k{occurs_pull_trigger_0}.
occurs_1 :- &k{occurs_pull_trigger_1}.
occurs_2 :- &k{occurs_pull_trigger_2}.
occurs_3 :- &k{occurs_pull_trigger_3}.
occurs_4 :- &k{occurs_pull_trigger_4}.
occurs_5 :- &k{occurs_pull_trigger_5}.
occurs_6 :- &k{occurs_pull_trigger_6}.
occurs_0 :- &k{occurs_aim_0}.
occurs_1 :- &k{occurs_aim_1}.
occurs_2 :- &k{occurs_aim_2}.
occurs_3 :- &k{occurs_aim_3}.
occurs_4 :- &k{occurs_aim_4}.
occurs_5 :- &k{occurs_aim_5}.
occurs_6 :- &k{occurs_aim_6}.
false :- not occurs_0.
false :- not occurs_1.
false :- not occurs_2.
false :- not occurs_3.
false :- not occurs_4.
false :- not occurs_5.
false :- not occurs_6.
occurs_load_0 :- not &k{ not occurs_load_0}.
occurs_load_1 :- not &k{ not occurs_load_1}.
occurs_load_2 :- not &k{ not occurs_load_2}.
occurs_load_3 :- not &k{ not occurs_load_3}.
occurs_load_4 :- not &k{ not occurs_load_4}.
occurs_load_5 :- not &k{ not occurs_load_5}.
occurs_load_6 :- not &k{ not occurs_load_6}.
occurs_pull_trigger_0 :- not &k{ not occurs_pull_trigger_0}.
occurs_pull_trigger_1 :- not &k{ not occurs_pull_trigger_1}.
occurs_pull_trigger_2 :- not &k{ not occurs_pull_trigger_2}.
occurs_pull_trigger_3 :- not &k{ not occurs_pull_trigger_3}.
occurs_pull_trigger_4 :- not &k{ not occurs_pull_trigger_4}.
occurs_pull_trigger_5 :- not &k{ not occurs_pull_trigger_5}.
occurs_pull_trigger_6 :- not &k{ not occurs_pull_trigger_6}.
occurs_aim_0 :- not &k{ not occurs_aim_0}.
occurs_aim_1 :- not &k{ not occurs_aim_1}.
occurs_aim_2 :- not &k{ not occurs_aim_2}.
occurs_aim_3 :- not &k{ not occurs_aim_3}.
occurs_aim_4 :- not &k{ not occurs_aim_4}.
occurs_aim_5 :- not &k{ not occurs_aim_5}.
occurs_aim_6 :- not &k{ not occurs_aim_6}.
ggoal :- &k{goal}.
false :- not ggoal.
executable_pull_trigger_0.
executable_pull_trigger_1.
executable_pull_trigger_2.
executable_pull_trigger_3.
executable_pull_trigger_4.
executable_pull_trigger_5.
executable_pull_trigger_6.
nholds_loaded_1 :- occurs_pull_trigger_0.
nholds_loaded_2 :- occurs_pull_trigger_1.
nholds_loaded_3 :- occurs_pull_trigger_2.
nholds_loaded_4 :- occurs_pull_trigger_3.
nholds_loaded_5 :- occurs_pull_trigger_4.
nholds_loaded_6 :- occurs_pull_trigger_5.
nholds_loaded_7 :- occurs_pull_trigger_6.
holds_loaded_1 :- occurs_load_0.
holds_loaded_2 :- occurs_load_1.
holds_loaded_3 :- occurs_load_2.
holds_loaded_4 :- occurs_load_3.
holds_loaded_5 :- occurs_load_4.
holds_loaded_6 :- occurs_load_5.
holds_loaded_7 :- occurs_load_6.
nholds_aimed_1 :- occurs_load_0.
nholds_aimed_2 :- occurs_load_1.
nholds_aimed_3 :- occurs_load_2.
nholds_aimed_4 :- occurs_load_3.
nholds_aimed_5 :- occurs_load_4.
nholds_aimed_6 :- occurs_load_5.
nholds_aimed_7 :- occurs_load_6.
nholds_aimed_1 :- occurs_pull_trigger_0.
nholds_aimed_2 :- occurs_pull_trigger_1.
nholds_aimed_3 :- occurs_pull_trigger_2.
nholds_aimed_4 :- occurs_pull_trigger_3.
nholds_aimed_5 :- occurs_pull_trigger_4.
nholds_aimed_6 :- occurs_pull_trigger_5.
nholds_aimed_7 :- occurs_pull_trigger_6.
holds_aimed_1 :- occurs_aim_0.
holds_aimed_2 :- occurs_aim_1.
holds_aimed_3 :- occurs_aim_2.
holds_aimed_4 :- occurs_aim_3.
holds_aimed_5 :- occurs_aim_4.
holds_aimed_6 :- occurs_aim_5.
holds_aimed_7 :- occurs_aim_6.
nholds_loaded_0 :- not holds_loaded_0.
holds_loaded_0 :- not nholds_loaded_0.
holds_aimed_0 :- not nholds_aimed_0.
nholds_loaded_0 :- not holds_loaded_0.
nholds_aimed_0 :- not holds_aimed_0.
nholds_aimed_0 :- not holds_aimed_0.
holds_wounded_1 :- holds_aimed_0, holds_loaded_0, occurs_pull_trigger_0.
holds_loaded_1 :- holds_loaded_0, not nholds_loaded_1.
holds_aimed_1 :- holds_aimed_0, not nholds_aimed_1.
holds_aimed_7 :- holds_aimed_6, not nholds_aimed_7.
holds_aimed_6 :- holds_aimed_5, not nholds_aimed_6.
holds_aimed_5 :- holds_aimed_4, not nholds_aimed_5.
holds_aimed_4 :- holds_aimed_3, not nholds_aimed_4.
holds_aimed_3 :- holds_aimed_2, not nholds_aimed_3.
holds_aimed_2 :- holds_aimed_1, not nholds_aimed_2.
holds_loaded_7 :- holds_loaded_6, not nholds_loaded_7.
holds_loaded_6 :- holds_loaded_5, not nholds_loaded_6.
holds_loaded_5 :- holds_loaded_4, not nholds_loaded_5.
holds_loaded_4 :- holds_loaded_3, not nholds_loaded_4.
holds_loaded_3 :- holds_loaded_2, not nholds_loaded_3.
holds_loaded_2 :- holds_loaded_1, not nholds_loaded_2.
holds_alive_1 :- not nholds_alive_1.
nholds_aimed_1 :- nholds_aimed_0, not holds_aimed_1.
nholds_loaded_1 :- nholds_loaded_0, not holds_loaded_1.
nholds_aimed_7 :- nholds_aimed_6, not holds_aimed_7.
nholds_aimed_6 :- nholds_aimed_5, not holds_aimed_6.
nholds_aimed_5 :- nholds_aimed_4, not holds_aimed_5.
nholds_aimed_4 :- nholds_aimed_3, not holds_aimed_4.
nholds_aimed_3 :- nholds_aimed_2, not holds_aimed_3.
nholds_aimed_2 :- nholds_aimed_1, not holds_aimed_2.
nholds_loaded_7 :- nholds_loaded_6, not holds_loaded_7.
nholds_loaded_6 :- nholds_loaded_5, not holds_loaded_6.
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
holds_alive_6 :- holds_alive_5, not nholds_alive_6.
holds_wounded_6 :- holds_wounded_5, not nholds_wounded_6.
nholds_alive_6 :- holds_aimed_5, holds_wounded_5, holds_loaded_5, occurs_pull_trigger_5.
holds_wounded_6 :- holds_aimed_5, holds_alive_5, nholds_wounded_5, holds_loaded_5, occurs_pull_trigger_5.
nholds_alive_6 :- nholds_alive_5, not holds_alive_6.
nholds_wounded_6 :- nholds_wounded_5, not holds_wounded_6.
holds_wounded_7 :- holds_aimed_6, holds_alive_6, nholds_wounded_6, holds_loaded_6, occurs_pull_trigger_6.
holds_wounded_7 :- holds_wounded_6, not nholds_wounded_7.
holds_alive_7 :- holds_alive_6, not nholds_alive_7.
nholds_alive_7 :- holds_aimed_6, holds_wounded_6, holds_loaded_6, occurs_pull_trigger_6.
nholds_wounded_7 :- nholds_wounded_6, not holds_wounded_7.
nholds_alive_7 :- nholds_alive_6, not holds_alive_7.
executable_load_1 :- nholds_loaded_1.
executable_load_2 :- nholds_loaded_2.
executable_load_3 :- nholds_loaded_3.
executable_load_4 :- nholds_loaded_4.
executable_load_5 :- nholds_loaded_5.
executable_load_6 :- nholds_loaded_6.
executable_load_0 :- nholds_loaded_0.
executable_aim_0.
executable_aim_1.
executable_aim_2.
executable_aim_3.
executable_aim_4.
executable_aim_5.
executable_aim_6.
imposs :- occurs_load_0, not executable_load_0.
imposs :- occurs_load_1, not executable_load_1.
imposs :- occurs_load_2, not executable_load_2.
imposs :- occurs_load_3, not executable_load_3.
imposs :- occurs_load_4, not executable_load_4.
imposs :- occurs_load_5, not executable_load_5.
imposs :- occurs_load_6, not executable_load_6.
goal :- not imposs, nholds_alive_7.
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
false :- occurs_load_5, occurs_pull_trigger_5.
false :- occurs_load_5, occurs_aim_5.
false :- occurs_load_6, occurs_pull_trigger_6.
false :- occurs_load_6, occurs_aim_6.
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
false :- occurs_pull_trigger_5, occurs_load_5.
false :- occurs_pull_trigger_5, occurs_aim_5.
false :- occurs_pull_trigger_6, occurs_load_6.
false :- occurs_pull_trigger_6, occurs_aim_6.
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
false :- occurs_aim_5, occurs_load_5.
false :- occurs_aim_5, occurs_pull_trigger_5.
false :- occurs_aim_6, occurs_load_6.
false :- occurs_aim_6, occurs_pull_trigger_6.
false :- nholds_loaded_1, holds_loaded_1.
false :- nholds_loaded_2, holds_loaded_2.
false :- nholds_loaded_3, holds_loaded_3.
false :- nholds_loaded_4, holds_loaded_4.
false :- nholds_loaded_5, holds_loaded_5.
false :- nholds_loaded_6, holds_loaded_6.
false :- nholds_loaded_7, holds_loaded_7.
false :- nholds_aimed_1, holds_aimed_1.
false :- nholds_aimed_2, holds_aimed_2.
false :- nholds_aimed_3, holds_aimed_3.
false :- nholds_aimed_4, holds_aimed_4.
false :- nholds_aimed_5, holds_aimed_5.
false :- nholds_aimed_6, holds_aimed_6.
false :- nholds_aimed_7, holds_aimed_7.
false :- nholds_loaded_0, holds_loaded_0.
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
false :- nholds_alive_6, holds_alive_6.
false :- nholds_wounded_6, holds_wounded_6.
false :- nholds_wounded_7, holds_wounded_7.
false :- nholds_alive_7, holds_alive_7.
