import clingo
from eclingo.parsing import ECLINGO_PREFIX, ECLINGO_PREFIX_U, ECLINGO_PREFIX_K, ECLINGO_PREFIX_NOT
from eclingo.parsing import ECLINGO_PREFIX_SN

a  = clingo.Function(ECLINGO_PREFIX_U + 'a', [], True)
b  = clingo.Function(ECLINGO_PREFIX_U + 'b', [], True)
c  = clingo.Function(ECLINGO_PREFIX_U + 'c', [], True)
d  = clingo.Function(ECLINGO_PREFIX_U + 'd', [], True)
e  = clingo.Function(ECLINGO_PREFIX_U + 'e', [], True)
f  = clingo.Function(ECLINGO_PREFIX_U + 'f', [], True)

sna  = clingo.Function(ECLINGO_PREFIX_U + 'a', [], False)
snb  = clingo.Function(ECLINGO_PREFIX_U + 'b', [], False)
snc  = clingo.Function(ECLINGO_PREFIX_U + 'c', [], False)
snd  = clingo.Function(ECLINGO_PREFIX_U + 'd', [], False)
sne  = clingo.Function(ECLINGO_PREFIX_U + 'e', [], False)
snf  = clingo.Function(ECLINGO_PREFIX_U + 'f', [], False)

ec_sna  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'a', [], True)
ec_snb  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'b', [], True)
ec_snc  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'c', [], True)
ec_snd  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'd', [], True)
ec_sne  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'e', [], True)
ec_snf  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_SN + 'f', [], True)

ka = clingo.Function(ECLINGO_PREFIX_K + 'a', [], True)
kb = clingo.Function(ECLINGO_PREFIX_K + 'b', [], True)
kc = clingo.Function(ECLINGO_PREFIX_K + 'c', [], True)
kd = clingo.Function(ECLINGO_PREFIX_K + 'd', [], True)
ke = clingo.Function(ECLINGO_PREFIX_K + 'e', [], True)
kf = clingo.Function(ECLINGO_PREFIX_K + 'f', [], True)

ksna = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'a', [], True)
ksnb = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'b', [], True)
ksnc = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'c', [], True)
ksnd = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'd', [], True)
ksne = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'e', [], True)
ksnf = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_SN + 'f', [], True)

nota  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'a', [], True)
notb  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'b', [], True)
notc  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'c', [], True)
notd  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'd', [], True)
note  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'e', [], True)
notf  = clingo.Function(ECLINGO_PREFIX + ECLINGO_PREFIX_NOT + 'f', [], True)

eclingo_prefix_not2 = ECLINGO_PREFIX_NOT + ECLINGO_PREFIX_NOT

not2a  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'a', [], True)
not2b  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'b', [], True)
not2c  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'c', [], True)
not2d  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'd', [], True)
not2e  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'e', [], True)
not2f  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2 + 'f', [], True)

eclingo_prefix_notsn = ECLINGO_PREFIX_NOT + ECLINGO_PREFIX_SN

notsna  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'a', [], True)
notsnb  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'b', [], True)
notsnc  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'c', [], True)
notsnd  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'd', [], True)
notsne  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'e', [], True)
notsnf  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_notsn + 'f', [], True)

eclingo_prefix_not2sn = eclingo_prefix_not2 + ECLINGO_PREFIX_SN

not2sna  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'a', [], True)
not2snb  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'b', [], True)
not2snc  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'c', [], True)
not2snd  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'd', [], True)
not2sne  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'e', [], True)
not2snf  = clingo.Function(ECLINGO_PREFIX + eclingo_prefix_not2sn + 'f', [], True)

knota = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'a', [], True)
knotb = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'b', [], True)
knotc = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'c', [], True)
knotd = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'd', [], True)
knote = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'e', [], True)
knotf = clingo.Function(ECLINGO_PREFIX_K + ECLINGO_PREFIX_NOT + 'f', [], True)

knotsna = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'a', [], True)
knotsnb = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'b', [], True)
knotsnc = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'c', [], True)
knotsnd = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'd', [], True)
knotsne = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'e', [], True)
knotsnf = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_notsn + 'f', [], True)

knot2a = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'a', [], True)
knot2b = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'b', [], True)
knot2c = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'c', [], True)
knot2d = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'd', [], True)
knot2e = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'e', [], True)
knot2f = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2 + 'f', [], True)

knot2sna = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'a', [], True)
knot2snb = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'b', [], True)
knot2snc = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'c', [], True)
knot2snd = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'd', [], True)
knot2sne = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'e', [], True)
knot2snf = clingo.Function(ECLINGO_PREFIX_K + eclingo_prefix_not2sn + 'f', [], True)
