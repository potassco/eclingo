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
variable(variable("f11")).
variable(variable("f12")).
variable(variable("f13")).
variable(variable("f14")).
variable(variable("f15")).
variable(variable("f16")).
variable(variable("f17")).
variable(variable("f18")).
variable(variable("f19")).
variable(variable("f20")).
variable(variable("f21")).
variable(variable("f22")).
variable(variable("f23")).
variable(variable("f24")).
variable(variable("f25")).
variable(variable("f26")).
variable(variable("f27")).
variable(variable("f28")).
variable(variable("f29")).
variable(variable("f30")).
variable(variable("f31")).
variable(variable("f32")).
variable(variable("f33")).
variable(variable("f34")).
variable(variable("f35")).
variable(variable("f36")).
variable(variable("f37")).
variable(variable("f38")).
variable(variable("f39")).
variable(variable("f40")).
variable(variable("f41")).
variable(variable("f42")).
variable(variable("f43")).
variable(variable("f44")).
variable(variable("f45")).
variable(variable("f46")).
variable(variable("f47")).
variable(variable("f48")).
variable(variable("f49")).
variable(variable("f50")).
variable(variable("f51")).
variable(variable("f52")).
variable(variable("f53")).
variable(variable("f54")).
variable(variable("f55")).
variable(variable("f56")).
variable(variable("f57")).
variable(variable("f58")).
variable(variable("f59")).
variable(variable("f60")).
variable(variable("f61")).
variable(variable("f62")).
variable(variable("f63")).
variable(variable("f64")).
variable(variable("f65")).
variable(variable("f66")).
variable(variable("f67")).
variable(variable("f68")).
variable(variable("f69")).
variable(variable("f70")).
variable(variable("f71")).
variable(variable("f72")).
variable(variable("f73")).
variable(variable("f74")).
variable(variable("f75")).
variable(variable("f76")).
variable(variable("f77")).
variable(variable("f78")).
variable(variable("f79")).
variable(variable("f80")).
variable(variable("f81")).
variable(variable("f82")).
variable(variable("f83")).
variable(variable("f84")).
variable(variable("f85")).
variable(variable("f86")).
variable(variable("f87")).
variable(variable("f88")).
variable(variable("f89")).
variable(variable("f90")).
variable(variable("f91")).
variable(variable("f92")).
variable(variable("f93")).
variable(variable("f94")).
variable(variable("f95")).
variable(variable("f96")).
variable(variable("f97")).
variable(variable("f98")).
variable(variable("f99")).
variable(variable("f100")).
variable(variable("f101")).
variable(variable("f102")).
variable(variable("f103")).
variable(variable("f104")).
variable(variable("f105")).
variable(variable("f106")).
variable(variable("f107")).
variable(variable("f108")).
variable(variable("f109")).
variable(variable("f110")).
variable(variable("f111")).
variable(variable("f112")).
variable(variable("f113")).
variable(variable("f114")).
variable(variable("f115")).
variable(variable("f116")).
variable(variable("f117")).
variable(variable("f118")).
variable(variable("f119")).
variable(variable("f120")).
variable(variable("f121")).
variable(variable("f122")).
variable(variable("f123")).
variable(variable("f124")).
variable(variable("f125")).
variable(variable("f126")).
variable(variable("f127")).
variable(variable("f128")).
variable(variable("f129")).
variable(variable("f130")).
variable(variable("f131")).
variable(variable("f132")).
variable(variable("f133")).
variable(variable("f134")).
variable(variable("f135")).
variable(variable("f136")).
variable(variable("f137")).
variable(variable("f138")).
variable(variable("f139")).
variable(variable("f140")).
variable(variable("f141")).
variable(variable("f142")).
variable(variable("f143")).
variable(variable("f144")).
variable(variable("f145")).
variable(variable("f146")).
variable(variable("f147")).
variable(variable("f148")).
variable(variable("f149")).
variable(variable("f150")).
variable(variable("f151")).
variable(variable("f152")).
variable(variable("f153")).
variable(variable("f154")).
variable(variable("f155")).
variable(variable("f156")).
variable(variable("f157")).
variable(variable("f158")).
variable(variable("f159")).
variable(variable("f160")).
variable(variable("f161")).
variable(variable("f162")).
variable(variable("f163")).
variable(variable("f164")).
variable(variable("f165")).
variable(variable("f166")).
variable(variable("f167")).
variable(variable("f168")).
variable(variable("f169")).
variable(variable("f170")).
variable(variable("f171")).
variable(variable("f172")).
variable(variable("f173")).
variable(variable("f174")).
variable(variable("f175")).
variable(variable("f176")).
variable(variable("f177")).
variable(variable("f178")).
variable(variable("f179")).
variable(variable("f180")).
variable(variable("f181")).
variable(variable("f182")).
variable(variable("f183")).
variable(variable("f184")).
variable(variable("f185")).
variable(variable("f186")).
variable(variable("f187")).
variable(variable("f188")).
variable(variable("f189")).
variable(variable("f190")).
variable(variable("f191")).
variable(variable("f192")).
variable(variable("f193")).
variable(variable("f194")).
variable(variable("f195")).
variable(variable("f196")).
variable(variable("f197")).
variable(variable("f198")).
variable(variable("f199")).
variable(variable("f200")).
variable(variable("f201")).
variable(variable("f202")).
variable(variable("f203")).
variable(variable("f204")).
variable(variable("f205")).
variable(variable("f206")).
variable(variable("f207")).
variable(variable("f208")).
variable(variable("f209")).
variable(variable("f210")).
variable(variable("f211")).
variable(variable("f212")).
variable(variable("f213")).
variable(variable("f214")).
variable(variable("f215")).
variable(variable("f216")).
variable(variable("f217")).
variable(variable("f218")).
variable(variable("f219")).
variable(variable("f220")).
variable(variable("f221")).
variable(variable("f222")).
variable(variable("f223")).
variable(variable("f224")).
variable(variable("f225")).
variable(variable("f226")).
variable(variable("f227")).
variable(variable("f228")).
variable(variable("f229")).
variable(variable("f230")).
variable(variable("f231")).
variable(variable("f232")).
variable(variable("f233")).
variable(variable("f234")).
variable(variable("f235")).
variable(variable("f236")).
variable(variable("f237")).
variable(variable("f238")).
variable(variable("f239")).
variable(variable("f240")).

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
precondition(action("del-all"), variable("f11"), value(variable("f11"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f12"), value(variable("f12"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f13"), value(variable("f13"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f14"), value(variable("f14"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f15"), value(variable("f15"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f16"), value(variable("f16"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f17"), value(variable("f17"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f18"), value(variable("f18"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f19"), value(variable("f19"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f20"), value(variable("f20"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f21"), value(variable("f21"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f22"), value(variable("f22"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f23"), value(variable("f23"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f24"), value(variable("f24"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f25"), value(variable("f25"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f26"), value(variable("f26"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f27"), value(variable("f27"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f28"), value(variable("f28"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f29"), value(variable("f29"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f30"), value(variable("f30"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f31"), value(variable("f31"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f32"), value(variable("f32"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f33"), value(variable("f33"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f34"), value(variable("f34"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f35"), value(variable("f35"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f36"), value(variable("f36"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f37"), value(variable("f37"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f38"), value(variable("f38"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f39"), value(variable("f39"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f40"), value(variable("f40"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f41"), value(variable("f41"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f42"), value(variable("f42"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f43"), value(variable("f43"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f44"), value(variable("f44"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f45"), value(variable("f45"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f46"), value(variable("f46"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f47"), value(variable("f47"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f48"), value(variable("f48"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f49"), value(variable("f49"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f50"), value(variable("f50"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f51"), value(variable("f51"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f52"), value(variable("f52"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f53"), value(variable("f53"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f54"), value(variable("f54"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f55"), value(variable("f55"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f56"), value(variable("f56"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f57"), value(variable("f57"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f58"), value(variable("f58"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f59"), value(variable("f59"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f60"), value(variable("f60"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f61"), value(variable("f61"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f62"), value(variable("f62"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f63"), value(variable("f63"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f64"), value(variable("f64"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f65"), value(variable("f65"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f66"), value(variable("f66"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f67"), value(variable("f67"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f68"), value(variable("f68"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f69"), value(variable("f69"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f70"), value(variable("f70"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f71"), value(variable("f71"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f72"), value(variable("f72"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f73"), value(variable("f73"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f74"), value(variable("f74"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f75"), value(variable("f75"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f76"), value(variable("f76"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f77"), value(variable("f77"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f78"), value(variable("f78"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f79"), value(variable("f79"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f80"), value(variable("f80"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f81"), value(variable("f81"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f82"), value(variable("f82"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f83"), value(variable("f83"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f84"), value(variable("f84"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f85"), value(variable("f85"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f86"), value(variable("f86"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f87"), value(variable("f87"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f88"), value(variable("f88"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f89"), value(variable("f89"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f90"), value(variable("f90"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f91"), value(variable("f91"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f92"), value(variable("f92"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f93"), value(variable("f93"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f94"), value(variable("f94"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f95"), value(variable("f95"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f96"), value(variable("f96"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f97"), value(variable("f97"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f98"), value(variable("f98"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f99"), value(variable("f99"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f100"), value(variable("f100"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f101"), value(variable("f101"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f102"), value(variable("f102"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f103"), value(variable("f103"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f104"), value(variable("f104"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f105"), value(variable("f105"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f106"), value(variable("f106"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f107"), value(variable("f107"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f108"), value(variable("f108"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f109"), value(variable("f109"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f110"), value(variable("f110"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f111"), value(variable("f111"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f112"), value(variable("f112"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f113"), value(variable("f113"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f114"), value(variable("f114"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f115"), value(variable("f115"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f116"), value(variable("f116"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f117"), value(variable("f117"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f118"), value(variable("f118"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f119"), value(variable("f119"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f120"), value(variable("f120"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f121"), value(variable("f121"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f122"), value(variable("f122"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f123"), value(variable("f123"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f124"), value(variable("f124"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f125"), value(variable("f125"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f126"), value(variable("f126"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f127"), value(variable("f127"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f128"), value(variable("f128"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f129"), value(variable("f129"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f130"), value(variable("f130"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f131"), value(variable("f131"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f132"), value(variable("f132"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f133"), value(variable("f133"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f134"), value(variable("f134"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f135"), value(variable("f135"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f136"), value(variable("f136"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f137"), value(variable("f137"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f138"), value(variable("f138"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f139"), value(variable("f139"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f140"), value(variable("f140"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f141"), value(variable("f141"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f142"), value(variable("f142"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f143"), value(variable("f143"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f144"), value(variable("f144"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f145"), value(variable("f145"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f146"), value(variable("f146"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f147"), value(variable("f147"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f148"), value(variable("f148"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f149"), value(variable("f149"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f150"), value(variable("f150"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f151"), value(variable("f151"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f152"), value(variable("f152"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f153"), value(variable("f153"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f154"), value(variable("f154"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f155"), value(variable("f155"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f156"), value(variable("f156"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f157"), value(variable("f157"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f158"), value(variable("f158"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f159"), value(variable("f159"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f160"), value(variable("f160"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f161"), value(variable("f161"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f162"), value(variable("f162"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f163"), value(variable("f163"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f164"), value(variable("f164"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f165"), value(variable("f165"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f166"), value(variable("f166"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f167"), value(variable("f167"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f168"), value(variable("f168"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f169"), value(variable("f169"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f170"), value(variable("f170"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f171"), value(variable("f171"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f172"), value(variable("f172"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f173"), value(variable("f173"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f174"), value(variable("f174"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f175"), value(variable("f175"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f176"), value(variable("f176"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f177"), value(variable("f177"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f178"), value(variable("f178"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f179"), value(variable("f179"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f180"), value(variable("f180"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f181"), value(variable("f181"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f182"), value(variable("f182"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f183"), value(variable("f183"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f184"), value(variable("f184"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f185"), value(variable("f185"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f186"), value(variable("f186"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f187"), value(variable("f187"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f188"), value(variable("f188"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f189"), value(variable("f189"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f190"), value(variable("f190"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f191"), value(variable("f191"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f192"), value(variable("f192"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f193"), value(variable("f193"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f194"), value(variable("f194"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f195"), value(variable("f195"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f196"), value(variable("f196"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f197"), value(variable("f197"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f198"), value(variable("f198"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f199"), value(variable("f199"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f200"), value(variable("f200"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f201"), value(variable("f201"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f202"), value(variable("f202"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f203"), value(variable("f203"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f204"), value(variable("f204"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f205"), value(variable("f205"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f206"), value(variable("f206"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f207"), value(variable("f207"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f208"), value(variable("f208"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f209"), value(variable("f209"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f210"), value(variable("f210"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f211"), value(variable("f211"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f212"), value(variable("f212"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f213"), value(variable("f213"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f214"), value(variable("f214"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f215"), value(variable("f215"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f216"), value(variable("f216"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f217"), value(variable("f217"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f218"), value(variable("f218"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f219"), value(variable("f219"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f220"), value(variable("f220"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f221"), value(variable("f221"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f222"), value(variable("f222"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f223"), value(variable("f223"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f224"), value(variable("f224"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f225"), value(variable("f225"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f226"), value(variable("f226"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f227"), value(variable("f227"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f228"), value(variable("f228"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f229"), value(variable("f229"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f230"), value(variable("f230"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f231"), value(variable("f231"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f232"), value(variable("f232"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f233"), value(variable("f233"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f234"), value(variable("f234"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f235"), value(variable("f235"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f236"), value(variable("f236"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f237"), value(variable("f237"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f238"), value(variable("f238"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f239"), value(variable("f239"), true)) :- action(action("del-all")).
precondition(action("del-all"), variable("f240"), value(variable("f240"), true)) :- action(action("del-all")).
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
postcondition(action("del-all"), effect(unconditional), variable("f11"), value(variable("f11"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f12"), value(variable("f12"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f13"), value(variable("f13"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f14"), value(variable("f14"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f15"), value(variable("f15"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f16"), value(variable("f16"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f17"), value(variable("f17"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f18"), value(variable("f18"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f19"), value(variable("f19"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f20"), value(variable("f20"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f21"), value(variable("f21"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f22"), value(variable("f22"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f23"), value(variable("f23"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f24"), value(variable("f24"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f25"), value(variable("f25"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f26"), value(variable("f26"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f27"), value(variable("f27"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f28"), value(variable("f28"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f29"), value(variable("f29"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f30"), value(variable("f30"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f31"), value(variable("f31"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f32"), value(variable("f32"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f33"), value(variable("f33"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f34"), value(variable("f34"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f35"), value(variable("f35"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f36"), value(variable("f36"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f37"), value(variable("f37"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f38"), value(variable("f38"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f39"), value(variable("f39"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f40"), value(variable("f40"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f41"), value(variable("f41"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f42"), value(variable("f42"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f43"), value(variable("f43"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f44"), value(variable("f44"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f45"), value(variable("f45"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f46"), value(variable("f46"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f47"), value(variable("f47"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f48"), value(variable("f48"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f49"), value(variable("f49"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f50"), value(variable("f50"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f51"), value(variable("f51"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f52"), value(variable("f52"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f53"), value(variable("f53"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f54"), value(variable("f54"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f55"), value(variable("f55"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f56"), value(variable("f56"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f57"), value(variable("f57"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f58"), value(variable("f58"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f59"), value(variable("f59"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f60"), value(variable("f60"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f61"), value(variable("f61"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f62"), value(variable("f62"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f63"), value(variable("f63"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f64"), value(variable("f64"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f65"), value(variable("f65"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f66"), value(variable("f66"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f67"), value(variable("f67"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f68"), value(variable("f68"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f69"), value(variable("f69"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f70"), value(variable("f70"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f71"), value(variable("f71"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f72"), value(variable("f72"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f73"), value(variable("f73"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f74"), value(variable("f74"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f75"), value(variable("f75"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f76"), value(variable("f76"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f77"), value(variable("f77"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f78"), value(variable("f78"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f79"), value(variable("f79"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f80"), value(variable("f80"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f81"), value(variable("f81"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f82"), value(variable("f82"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f83"), value(variable("f83"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f84"), value(variable("f84"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f85"), value(variable("f85"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f86"), value(variable("f86"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f87"), value(variable("f87"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f88"), value(variable("f88"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f89"), value(variable("f89"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f90"), value(variable("f90"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f91"), value(variable("f91"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f92"), value(variable("f92"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f93"), value(variable("f93"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f94"), value(variable("f94"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f95"), value(variable("f95"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f96"), value(variable("f96"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f97"), value(variable("f97"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f98"), value(variable("f98"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f99"), value(variable("f99"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f100"), value(variable("f100"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f101"), value(variable("f101"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f102"), value(variable("f102"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f103"), value(variable("f103"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f104"), value(variable("f104"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f105"), value(variable("f105"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f106"), value(variable("f106"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f107"), value(variable("f107"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f108"), value(variable("f108"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f109"), value(variable("f109"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f110"), value(variable("f110"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f111"), value(variable("f111"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f112"), value(variable("f112"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f113"), value(variable("f113"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f114"), value(variable("f114"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f115"), value(variable("f115"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f116"), value(variable("f116"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f117"), value(variable("f117"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f118"), value(variable("f118"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f119"), value(variable("f119"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f120"), value(variable("f120"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f121"), value(variable("f121"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f122"), value(variable("f122"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f123"), value(variable("f123"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f124"), value(variable("f124"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f125"), value(variable("f125"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f126"), value(variable("f126"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f127"), value(variable("f127"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f128"), value(variable("f128"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f129"), value(variable("f129"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f130"), value(variable("f130"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f131"), value(variable("f131"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f132"), value(variable("f132"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f133"), value(variable("f133"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f134"), value(variable("f134"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f135"), value(variable("f135"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f136"), value(variable("f136"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f137"), value(variable("f137"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f138"), value(variable("f138"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f139"), value(variable("f139"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f140"), value(variable("f140"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f141"), value(variable("f141"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f142"), value(variable("f142"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f143"), value(variable("f143"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f144"), value(variable("f144"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f145"), value(variable("f145"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f146"), value(variable("f146"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f147"), value(variable("f147"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f148"), value(variable("f148"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f149"), value(variable("f149"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f150"), value(variable("f150"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f151"), value(variable("f151"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f152"), value(variable("f152"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f153"), value(variable("f153"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f154"), value(variable("f154"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f155"), value(variable("f155"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f156"), value(variable("f156"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f157"), value(variable("f157"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f158"), value(variable("f158"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f159"), value(variable("f159"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f160"), value(variable("f160"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f161"), value(variable("f161"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f162"), value(variable("f162"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f163"), value(variable("f163"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f164"), value(variable("f164"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f165"), value(variable("f165"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f166"), value(variable("f166"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f167"), value(variable("f167"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f168"), value(variable("f168"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f169"), value(variable("f169"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f170"), value(variable("f170"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f171"), value(variable("f171"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f172"), value(variable("f172"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f173"), value(variable("f173"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f174"), value(variable("f174"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f175"), value(variable("f175"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f176"), value(variable("f176"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f177"), value(variable("f177"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f178"), value(variable("f178"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f179"), value(variable("f179"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f180"), value(variable("f180"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f181"), value(variable("f181"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f182"), value(variable("f182"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f183"), value(variable("f183"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f184"), value(variable("f184"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f185"), value(variable("f185"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f186"), value(variable("f186"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f187"), value(variable("f187"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f188"), value(variable("f188"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f189"), value(variable("f189"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f190"), value(variable("f190"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f191"), value(variable("f191"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f192"), value(variable("f192"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f193"), value(variable("f193"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f194"), value(variable("f194"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f195"), value(variable("f195"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f196"), value(variable("f196"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f197"), value(variable("f197"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f198"), value(variable("f198"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f199"), value(variable("f199"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f200"), value(variable("f200"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f201"), value(variable("f201"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f202"), value(variable("f202"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f203"), value(variable("f203"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f204"), value(variable("f204"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f205"), value(variable("f205"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f206"), value(variable("f206"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f207"), value(variable("f207"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f208"), value(variable("f208"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f209"), value(variable("f209"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f210"), value(variable("f210"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f211"), value(variable("f211"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f212"), value(variable("f212"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f213"), value(variable("f213"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f214"), value(variable("f214"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f215"), value(variable("f215"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f216"), value(variable("f216"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f217"), value(variable("f217"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f218"), value(variable("f218"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f219"), value(variable("f219"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f220"), value(variable("f220"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f221"), value(variable("f221"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f222"), value(variable("f222"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f223"), value(variable("f223"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f224"), value(variable("f224"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f225"), value(variable("f225"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f226"), value(variable("f226"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f227"), value(variable("f227"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f228"), value(variable("f228"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f229"), value(variable("f229"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f230"), value(variable("f230"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f231"), value(variable("f231"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f232"), value(variable("f232"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f233"), value(variable("f233"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f234"), value(variable("f234"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f235"), value(variable("f235"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f236"), value(variable("f236"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f237"), value(variable("f237"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f238"), value(variable("f238"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f239"), value(variable("f239"), false)) :- action(action("del-all")).
postcondition(action("del-all"), effect(unconditional), variable("f240"), value(variable("f240"), false)) :- action(action("del-all")).

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

action(action("add-f11")).
precondition(action("add-f11"), variable("f10"), value(variable("f10"), true)) :- action(action("add-f11")).
postcondition(action("add-f11"), effect(unconditional), variable("f11"), value(variable("f11"), true)) :- action(action("add-f11")).

action(action("add-f12")).
precondition(action("add-f12"), variable("f11"), value(variable("f11"), true)) :- action(action("add-f12")).
postcondition(action("add-f12"), effect(unconditional), variable("f12"), value(variable("f12"), true)) :- action(action("add-f12")).

action(action("add-f13")).
precondition(action("add-f13"), variable("f12"), value(variable("f12"), true)) :- action(action("add-f13")).
postcondition(action("add-f13"), effect(unconditional), variable("f13"), value(variable("f13"), true)) :- action(action("add-f13")).

action(action("add-f14")).
precondition(action("add-f14"), variable("f13"), value(variable("f13"), true)) :- action(action("add-f14")).
postcondition(action("add-f14"), effect(unconditional), variable("f14"), value(variable("f14"), true)) :- action(action("add-f14")).

action(action("add-f15")).
precondition(action("add-f15"), variable("f14"), value(variable("f14"), true)) :- action(action("add-f15")).
postcondition(action("add-f15"), effect(unconditional), variable("f15"), value(variable("f15"), true)) :- action(action("add-f15")).

action(action("add-f16")).
precondition(action("add-f16"), variable("f15"), value(variable("f15"), true)) :- action(action("add-f16")).
postcondition(action("add-f16"), effect(unconditional), variable("f16"), value(variable("f16"), true)) :- action(action("add-f16")).

action(action("add-f17")).
precondition(action("add-f17"), variable("f16"), value(variable("f16"), true)) :- action(action("add-f17")).
postcondition(action("add-f17"), effect(unconditional), variable("f17"), value(variable("f17"), true)) :- action(action("add-f17")).

action(action("add-f18")).
precondition(action("add-f18"), variable("f17"), value(variable("f17"), true)) :- action(action("add-f18")).
postcondition(action("add-f18"), effect(unconditional), variable("f18"), value(variable("f18"), true)) :- action(action("add-f18")).

action(action("add-f19")).
precondition(action("add-f19"), variable("f18"), value(variable("f18"), true)) :- action(action("add-f19")).
postcondition(action("add-f19"), effect(unconditional), variable("f19"), value(variable("f19"), true)) :- action(action("add-f19")).

action(action("add-f20")).
precondition(action("add-f20"), variable("f19"), value(variable("f19"), true)) :- action(action("add-f20")).
postcondition(action("add-f20"), effect(unconditional), variable("f20"), value(variable("f20"), true)) :- action(action("add-f20")).

action(action("add-f21")).
precondition(action("add-f21"), variable("f20"), value(variable("f20"), true)) :- action(action("add-f21")).
postcondition(action("add-f21"), effect(unconditional), variable("f21"), value(variable("f21"), true)) :- action(action("add-f21")).

action(action("add-f22")).
precondition(action("add-f22"), variable("f21"), value(variable("f21"), true)) :- action(action("add-f22")).
postcondition(action("add-f22"), effect(unconditional), variable("f22"), value(variable("f22"), true)) :- action(action("add-f22")).

action(action("add-f23")).
precondition(action("add-f23"), variable("f22"), value(variable("f22"), true)) :- action(action("add-f23")).
postcondition(action("add-f23"), effect(unconditional), variable("f23"), value(variable("f23"), true)) :- action(action("add-f23")).

action(action("add-f24")).
precondition(action("add-f24"), variable("f23"), value(variable("f23"), true)) :- action(action("add-f24")).
postcondition(action("add-f24"), effect(unconditional), variable("f24"), value(variable("f24"), true)) :- action(action("add-f24")).

action(action("add-f25")).
precondition(action("add-f25"), variable("f24"), value(variable("f24"), true)) :- action(action("add-f25")).
postcondition(action("add-f25"), effect(unconditional), variable("f25"), value(variable("f25"), true)) :- action(action("add-f25")).

action(action("add-f26")).
precondition(action("add-f26"), variable("f25"), value(variable("f25"), true)) :- action(action("add-f26")).
postcondition(action("add-f26"), effect(unconditional), variable("f26"), value(variable("f26"), true)) :- action(action("add-f26")).

action(action("add-f27")).
precondition(action("add-f27"), variable("f26"), value(variable("f26"), true)) :- action(action("add-f27")).
postcondition(action("add-f27"), effect(unconditional), variable("f27"), value(variable("f27"), true)) :- action(action("add-f27")).

action(action("add-f28")).
precondition(action("add-f28"), variable("f27"), value(variable("f27"), true)) :- action(action("add-f28")).
postcondition(action("add-f28"), effect(unconditional), variable("f28"), value(variable("f28"), true)) :- action(action("add-f28")).

action(action("add-f29")).
precondition(action("add-f29"), variable("f28"), value(variable("f28"), true)) :- action(action("add-f29")).
postcondition(action("add-f29"), effect(unconditional), variable("f29"), value(variable("f29"), true)) :- action(action("add-f29")).

action(action("add-f30")).
precondition(action("add-f30"), variable("f29"), value(variable("f29"), true)) :- action(action("add-f30")).
postcondition(action("add-f30"), effect(unconditional), variable("f30"), value(variable("f30"), true)) :- action(action("add-f30")).

action(action("add-f31")).
precondition(action("add-f31"), variable("f30"), value(variable("f30"), true)) :- action(action("add-f31")).
postcondition(action("add-f31"), effect(unconditional), variable("f31"), value(variable("f31"), true)) :- action(action("add-f31")).

action(action("add-f32")).
precondition(action("add-f32"), variable("f31"), value(variable("f31"), true)) :- action(action("add-f32")).
postcondition(action("add-f32"), effect(unconditional), variable("f32"), value(variable("f32"), true)) :- action(action("add-f32")).

action(action("add-f33")).
precondition(action("add-f33"), variable("f32"), value(variable("f32"), true)) :- action(action("add-f33")).
postcondition(action("add-f33"), effect(unconditional), variable("f33"), value(variable("f33"), true)) :- action(action("add-f33")).

action(action("add-f34")).
precondition(action("add-f34"), variable("f33"), value(variable("f33"), true)) :- action(action("add-f34")).
postcondition(action("add-f34"), effect(unconditional), variable("f34"), value(variable("f34"), true)) :- action(action("add-f34")).

action(action("add-f35")).
precondition(action("add-f35"), variable("f34"), value(variable("f34"), true)) :- action(action("add-f35")).
postcondition(action("add-f35"), effect(unconditional), variable("f35"), value(variable("f35"), true)) :- action(action("add-f35")).

action(action("add-f36")).
precondition(action("add-f36"), variable("f35"), value(variable("f35"), true)) :- action(action("add-f36")).
postcondition(action("add-f36"), effect(unconditional), variable("f36"), value(variable("f36"), true)) :- action(action("add-f36")).

action(action("add-f37")).
precondition(action("add-f37"), variable("f36"), value(variable("f36"), true)) :- action(action("add-f37")).
postcondition(action("add-f37"), effect(unconditional), variable("f37"), value(variable("f37"), true)) :- action(action("add-f37")).

action(action("add-f38")).
precondition(action("add-f38"), variable("f37"), value(variable("f37"), true)) :- action(action("add-f38")).
postcondition(action("add-f38"), effect(unconditional), variable("f38"), value(variable("f38"), true)) :- action(action("add-f38")).

action(action("add-f39")).
precondition(action("add-f39"), variable("f38"), value(variable("f38"), true)) :- action(action("add-f39")).
postcondition(action("add-f39"), effect(unconditional), variable("f39"), value(variable("f39"), true)) :- action(action("add-f39")).

action(action("add-f40")).
precondition(action("add-f40"), variable("f39"), value(variable("f39"), true)) :- action(action("add-f40")).
postcondition(action("add-f40"), effect(unconditional), variable("f40"), value(variable("f40"), true)) :- action(action("add-f40")).

action(action("add-f41")).
precondition(action("add-f41"), variable("f40"), value(variable("f40"), true)) :- action(action("add-f41")).
postcondition(action("add-f41"), effect(unconditional), variable("f41"), value(variable("f41"), true)) :- action(action("add-f41")).

action(action("add-f42")).
precondition(action("add-f42"), variable("f41"), value(variable("f41"), true)) :- action(action("add-f42")).
postcondition(action("add-f42"), effect(unconditional), variable("f42"), value(variable("f42"), true)) :- action(action("add-f42")).

action(action("add-f43")).
precondition(action("add-f43"), variable("f42"), value(variable("f42"), true)) :- action(action("add-f43")).
postcondition(action("add-f43"), effect(unconditional), variable("f43"), value(variable("f43"), true)) :- action(action("add-f43")).

action(action("add-f44")).
precondition(action("add-f44"), variable("f43"), value(variable("f43"), true)) :- action(action("add-f44")).
postcondition(action("add-f44"), effect(unconditional), variable("f44"), value(variable("f44"), true)) :- action(action("add-f44")).

action(action("add-f45")).
precondition(action("add-f45"), variable("f44"), value(variable("f44"), true)) :- action(action("add-f45")).
postcondition(action("add-f45"), effect(unconditional), variable("f45"), value(variable("f45"), true)) :- action(action("add-f45")).

action(action("add-f46")).
precondition(action("add-f46"), variable("f45"), value(variable("f45"), true)) :- action(action("add-f46")).
postcondition(action("add-f46"), effect(unconditional), variable("f46"), value(variable("f46"), true)) :- action(action("add-f46")).

action(action("add-f47")).
precondition(action("add-f47"), variable("f46"), value(variable("f46"), true)) :- action(action("add-f47")).
postcondition(action("add-f47"), effect(unconditional), variable("f47"), value(variable("f47"), true)) :- action(action("add-f47")).

action(action("add-f48")).
precondition(action("add-f48"), variable("f47"), value(variable("f47"), true)) :- action(action("add-f48")).
postcondition(action("add-f48"), effect(unconditional), variable("f48"), value(variable("f48"), true)) :- action(action("add-f48")).

action(action("add-f49")).
precondition(action("add-f49"), variable("f48"), value(variable("f48"), true)) :- action(action("add-f49")).
postcondition(action("add-f49"), effect(unconditional), variable("f49"), value(variable("f49"), true)) :- action(action("add-f49")).

action(action("add-f50")).
precondition(action("add-f50"), variable("f49"), value(variable("f49"), true)) :- action(action("add-f50")).
postcondition(action("add-f50"), effect(unconditional), variable("f50"), value(variable("f50"), true)) :- action(action("add-f50")).

action(action("add-f51")).
precondition(action("add-f51"), variable("f50"), value(variable("f50"), true)) :- action(action("add-f51")).
postcondition(action("add-f51"), effect(unconditional), variable("f51"), value(variable("f51"), true)) :- action(action("add-f51")).

action(action("add-f52")).
precondition(action("add-f52"), variable("f51"), value(variable("f51"), true)) :- action(action("add-f52")).
postcondition(action("add-f52"), effect(unconditional), variable("f52"), value(variable("f52"), true)) :- action(action("add-f52")).

action(action("add-f53")).
precondition(action("add-f53"), variable("f52"), value(variable("f52"), true)) :- action(action("add-f53")).
postcondition(action("add-f53"), effect(unconditional), variable("f53"), value(variable("f53"), true)) :- action(action("add-f53")).

action(action("add-f54")).
precondition(action("add-f54"), variable("f53"), value(variable("f53"), true)) :- action(action("add-f54")).
postcondition(action("add-f54"), effect(unconditional), variable("f54"), value(variable("f54"), true)) :- action(action("add-f54")).

action(action("add-f55")).
precondition(action("add-f55"), variable("f54"), value(variable("f54"), true)) :- action(action("add-f55")).
postcondition(action("add-f55"), effect(unconditional), variable("f55"), value(variable("f55"), true)) :- action(action("add-f55")).

action(action("add-f56")).
precondition(action("add-f56"), variable("f55"), value(variable("f55"), true)) :- action(action("add-f56")).
postcondition(action("add-f56"), effect(unconditional), variable("f56"), value(variable("f56"), true)) :- action(action("add-f56")).

action(action("add-f57")).
precondition(action("add-f57"), variable("f56"), value(variable("f56"), true)) :- action(action("add-f57")).
postcondition(action("add-f57"), effect(unconditional), variable("f57"), value(variable("f57"), true)) :- action(action("add-f57")).

action(action("add-f58")).
precondition(action("add-f58"), variable("f57"), value(variable("f57"), true)) :- action(action("add-f58")).
postcondition(action("add-f58"), effect(unconditional), variable("f58"), value(variable("f58"), true)) :- action(action("add-f58")).

action(action("add-f59")).
precondition(action("add-f59"), variable("f58"), value(variable("f58"), true)) :- action(action("add-f59")).
postcondition(action("add-f59"), effect(unconditional), variable("f59"), value(variable("f59"), true)) :- action(action("add-f59")).

action(action("add-f60")).
precondition(action("add-f60"), variable("f59"), value(variable("f59"), true)) :- action(action("add-f60")).
postcondition(action("add-f60"), effect(unconditional), variable("f60"), value(variable("f60"), true)) :- action(action("add-f60")).

action(action("add-f61")).
precondition(action("add-f61"), variable("f60"), value(variable("f60"), true)) :- action(action("add-f61")).
postcondition(action("add-f61"), effect(unconditional), variable("f61"), value(variable("f61"), true)) :- action(action("add-f61")).

action(action("add-f62")).
precondition(action("add-f62"), variable("f61"), value(variable("f61"), true)) :- action(action("add-f62")).
postcondition(action("add-f62"), effect(unconditional), variable("f62"), value(variable("f62"), true)) :- action(action("add-f62")).

action(action("add-f63")).
precondition(action("add-f63"), variable("f62"), value(variable("f62"), true)) :- action(action("add-f63")).
postcondition(action("add-f63"), effect(unconditional), variable("f63"), value(variable("f63"), true)) :- action(action("add-f63")).

action(action("add-f64")).
precondition(action("add-f64"), variable("f63"), value(variable("f63"), true)) :- action(action("add-f64")).
postcondition(action("add-f64"), effect(unconditional), variable("f64"), value(variable("f64"), true)) :- action(action("add-f64")).

action(action("add-f65")).
precondition(action("add-f65"), variable("f64"), value(variable("f64"), true)) :- action(action("add-f65")).
postcondition(action("add-f65"), effect(unconditional), variable("f65"), value(variable("f65"), true)) :- action(action("add-f65")).

action(action("add-f66")).
precondition(action("add-f66"), variable("f65"), value(variable("f65"), true)) :- action(action("add-f66")).
postcondition(action("add-f66"), effect(unconditional), variable("f66"), value(variable("f66"), true)) :- action(action("add-f66")).

action(action("add-f67")).
precondition(action("add-f67"), variable("f66"), value(variable("f66"), true)) :- action(action("add-f67")).
postcondition(action("add-f67"), effect(unconditional), variable("f67"), value(variable("f67"), true)) :- action(action("add-f67")).

action(action("add-f68")).
precondition(action("add-f68"), variable("f67"), value(variable("f67"), true)) :- action(action("add-f68")).
postcondition(action("add-f68"), effect(unconditional), variable("f68"), value(variable("f68"), true)) :- action(action("add-f68")).

action(action("add-f69")).
precondition(action("add-f69"), variable("f68"), value(variable("f68"), true)) :- action(action("add-f69")).
postcondition(action("add-f69"), effect(unconditional), variable("f69"), value(variable("f69"), true)) :- action(action("add-f69")).

action(action("add-f70")).
precondition(action("add-f70"), variable("f69"), value(variable("f69"), true)) :- action(action("add-f70")).
postcondition(action("add-f70"), effect(unconditional), variable("f70"), value(variable("f70"), true)) :- action(action("add-f70")).

action(action("add-f71")).
precondition(action("add-f71"), variable("f70"), value(variable("f70"), true)) :- action(action("add-f71")).
postcondition(action("add-f71"), effect(unconditional), variable("f71"), value(variable("f71"), true)) :- action(action("add-f71")).

action(action("add-f72")).
precondition(action("add-f72"), variable("f71"), value(variable("f71"), true)) :- action(action("add-f72")).
postcondition(action("add-f72"), effect(unconditional), variable("f72"), value(variable("f72"), true)) :- action(action("add-f72")).

action(action("add-f73")).
precondition(action("add-f73"), variable("f72"), value(variable("f72"), true)) :- action(action("add-f73")).
postcondition(action("add-f73"), effect(unconditional), variable("f73"), value(variable("f73"), true)) :- action(action("add-f73")).

action(action("add-f74")).
precondition(action("add-f74"), variable("f73"), value(variable("f73"), true)) :- action(action("add-f74")).
postcondition(action("add-f74"), effect(unconditional), variable("f74"), value(variable("f74"), true)) :- action(action("add-f74")).

action(action("add-f75")).
precondition(action("add-f75"), variable("f74"), value(variable("f74"), true)) :- action(action("add-f75")).
postcondition(action("add-f75"), effect(unconditional), variable("f75"), value(variable("f75"), true)) :- action(action("add-f75")).

action(action("add-f76")).
precondition(action("add-f76"), variable("f75"), value(variable("f75"), true)) :- action(action("add-f76")).
postcondition(action("add-f76"), effect(unconditional), variable("f76"), value(variable("f76"), true)) :- action(action("add-f76")).

action(action("add-f77")).
precondition(action("add-f77"), variable("f76"), value(variable("f76"), true)) :- action(action("add-f77")).
postcondition(action("add-f77"), effect(unconditional), variable("f77"), value(variable("f77"), true)) :- action(action("add-f77")).

action(action("add-f78")).
precondition(action("add-f78"), variable("f77"), value(variable("f77"), true)) :- action(action("add-f78")).
postcondition(action("add-f78"), effect(unconditional), variable("f78"), value(variable("f78"), true)) :- action(action("add-f78")).

action(action("add-f79")).
precondition(action("add-f79"), variable("f78"), value(variable("f78"), true)) :- action(action("add-f79")).
postcondition(action("add-f79"), effect(unconditional), variable("f79"), value(variable("f79"), true)) :- action(action("add-f79")).

action(action("add-f80")).
precondition(action("add-f80"), variable("f79"), value(variable("f79"), true)) :- action(action("add-f80")).
postcondition(action("add-f80"), effect(unconditional), variable("f80"), value(variable("f80"), true)) :- action(action("add-f80")).

action(action("add-f81")).
precondition(action("add-f81"), variable("f80"), value(variable("f80"), true)) :- action(action("add-f81")).
postcondition(action("add-f81"), effect(unconditional), variable("f81"), value(variable("f81"), true)) :- action(action("add-f81")).

action(action("add-f82")).
precondition(action("add-f82"), variable("f81"), value(variable("f81"), true)) :- action(action("add-f82")).
postcondition(action("add-f82"), effect(unconditional), variable("f82"), value(variable("f82"), true)) :- action(action("add-f82")).

action(action("add-f83")).
precondition(action("add-f83"), variable("f82"), value(variable("f82"), true)) :- action(action("add-f83")).
postcondition(action("add-f83"), effect(unconditional), variable("f83"), value(variable("f83"), true)) :- action(action("add-f83")).

action(action("add-f84")).
precondition(action("add-f84"), variable("f83"), value(variable("f83"), true)) :- action(action("add-f84")).
postcondition(action("add-f84"), effect(unconditional), variable("f84"), value(variable("f84"), true)) :- action(action("add-f84")).

action(action("add-f85")).
precondition(action("add-f85"), variable("f84"), value(variable("f84"), true)) :- action(action("add-f85")).
postcondition(action("add-f85"), effect(unconditional), variable("f85"), value(variable("f85"), true)) :- action(action("add-f85")).

action(action("add-f86")).
precondition(action("add-f86"), variable("f85"), value(variable("f85"), true)) :- action(action("add-f86")).
postcondition(action("add-f86"), effect(unconditional), variable("f86"), value(variable("f86"), true)) :- action(action("add-f86")).

action(action("add-f87")).
precondition(action("add-f87"), variable("f86"), value(variable("f86"), true)) :- action(action("add-f87")).
postcondition(action("add-f87"), effect(unconditional), variable("f87"), value(variable("f87"), true)) :- action(action("add-f87")).

action(action("add-f88")).
precondition(action("add-f88"), variable("f87"), value(variable("f87"), true)) :- action(action("add-f88")).
postcondition(action("add-f88"), effect(unconditional), variable("f88"), value(variable("f88"), true)) :- action(action("add-f88")).

action(action("add-f89")).
precondition(action("add-f89"), variable("f88"), value(variable("f88"), true)) :- action(action("add-f89")).
postcondition(action("add-f89"), effect(unconditional), variable("f89"), value(variable("f89"), true)) :- action(action("add-f89")).

action(action("add-f90")).
precondition(action("add-f90"), variable("f89"), value(variable("f89"), true)) :- action(action("add-f90")).
postcondition(action("add-f90"), effect(unconditional), variable("f90"), value(variable("f90"), true)) :- action(action("add-f90")).

action(action("add-f91")).
precondition(action("add-f91"), variable("f90"), value(variable("f90"), true)) :- action(action("add-f91")).
postcondition(action("add-f91"), effect(unconditional), variable("f91"), value(variable("f91"), true)) :- action(action("add-f91")).

action(action("add-f92")).
precondition(action("add-f92"), variable("f91"), value(variable("f91"), true)) :- action(action("add-f92")).
postcondition(action("add-f92"), effect(unconditional), variable("f92"), value(variable("f92"), true)) :- action(action("add-f92")).

action(action("add-f93")).
precondition(action("add-f93"), variable("f92"), value(variable("f92"), true)) :- action(action("add-f93")).
postcondition(action("add-f93"), effect(unconditional), variable("f93"), value(variable("f93"), true)) :- action(action("add-f93")).

action(action("add-f94")).
precondition(action("add-f94"), variable("f93"), value(variable("f93"), true)) :- action(action("add-f94")).
postcondition(action("add-f94"), effect(unconditional), variable("f94"), value(variable("f94"), true)) :- action(action("add-f94")).

action(action("add-f95")).
precondition(action("add-f95"), variable("f94"), value(variable("f94"), true)) :- action(action("add-f95")).
postcondition(action("add-f95"), effect(unconditional), variable("f95"), value(variable("f95"), true)) :- action(action("add-f95")).

action(action("add-f96")).
precondition(action("add-f96"), variable("f95"), value(variable("f95"), true)) :- action(action("add-f96")).
postcondition(action("add-f96"), effect(unconditional), variable("f96"), value(variable("f96"), true)) :- action(action("add-f96")).

action(action("add-f97")).
precondition(action("add-f97"), variable("f96"), value(variable("f96"), true)) :- action(action("add-f97")).
postcondition(action("add-f97"), effect(unconditional), variable("f97"), value(variable("f97"), true)) :- action(action("add-f97")).

action(action("add-f98")).
precondition(action("add-f98"), variable("f97"), value(variable("f97"), true)) :- action(action("add-f98")).
postcondition(action("add-f98"), effect(unconditional), variable("f98"), value(variable("f98"), true)) :- action(action("add-f98")).

action(action("add-f99")).
precondition(action("add-f99"), variable("f98"), value(variable("f98"), true)) :- action(action("add-f99")).
postcondition(action("add-f99"), effect(unconditional), variable("f99"), value(variable("f99"), true)) :- action(action("add-f99")).

action(action("add-f100")).
precondition(action("add-f100"), variable("f99"), value(variable("f99"), true)) :- action(action("add-f100")).
postcondition(action("add-f100"), effect(unconditional), variable("f100"), value(variable("f100"), true)) :- action(action("add-f100")).

action(action("add-f101")).
precondition(action("add-f101"), variable("f100"), value(variable("f100"), true)) :- action(action("add-f101")).
postcondition(action("add-f101"), effect(unconditional), variable("f101"), value(variable("f101"), true)) :- action(action("add-f101")).

action(action("add-f102")).
precondition(action("add-f102"), variable("f101"), value(variable("f101"), true)) :- action(action("add-f102")).
postcondition(action("add-f102"), effect(unconditional), variable("f102"), value(variable("f102"), true)) :- action(action("add-f102")).

action(action("add-f103")).
precondition(action("add-f103"), variable("f102"), value(variable("f102"), true)) :- action(action("add-f103")).
postcondition(action("add-f103"), effect(unconditional), variable("f103"), value(variable("f103"), true)) :- action(action("add-f103")).

action(action("add-f104")).
precondition(action("add-f104"), variable("f103"), value(variable("f103"), true)) :- action(action("add-f104")).
postcondition(action("add-f104"), effect(unconditional), variable("f104"), value(variable("f104"), true)) :- action(action("add-f104")).

action(action("add-f105")).
precondition(action("add-f105"), variable("f104"), value(variable("f104"), true)) :- action(action("add-f105")).
postcondition(action("add-f105"), effect(unconditional), variable("f105"), value(variable("f105"), true)) :- action(action("add-f105")).

action(action("add-f106")).
precondition(action("add-f106"), variable("f105"), value(variable("f105"), true)) :- action(action("add-f106")).
postcondition(action("add-f106"), effect(unconditional), variable("f106"), value(variable("f106"), true)) :- action(action("add-f106")).

action(action("add-f107")).
precondition(action("add-f107"), variable("f106"), value(variable("f106"), true)) :- action(action("add-f107")).
postcondition(action("add-f107"), effect(unconditional), variable("f107"), value(variable("f107"), true)) :- action(action("add-f107")).

action(action("add-f108")).
precondition(action("add-f108"), variable("f107"), value(variable("f107"), true)) :- action(action("add-f108")).
postcondition(action("add-f108"), effect(unconditional), variable("f108"), value(variable("f108"), true)) :- action(action("add-f108")).

action(action("add-f109")).
precondition(action("add-f109"), variable("f108"), value(variable("f108"), true)) :- action(action("add-f109")).
postcondition(action("add-f109"), effect(unconditional), variable("f109"), value(variable("f109"), true)) :- action(action("add-f109")).

action(action("add-f110")).
precondition(action("add-f110"), variable("f109"), value(variable("f109"), true)) :- action(action("add-f110")).
postcondition(action("add-f110"), effect(unconditional), variable("f110"), value(variable("f110"), true)) :- action(action("add-f110")).

action(action("add-f111")).
precondition(action("add-f111"), variable("f110"), value(variable("f110"), true)) :- action(action("add-f111")).
postcondition(action("add-f111"), effect(unconditional), variable("f111"), value(variable("f111"), true)) :- action(action("add-f111")).

action(action("add-f112")).
precondition(action("add-f112"), variable("f111"), value(variable("f111"), true)) :- action(action("add-f112")).
postcondition(action("add-f112"), effect(unconditional), variable("f112"), value(variable("f112"), true)) :- action(action("add-f112")).

action(action("add-f113")).
precondition(action("add-f113"), variable("f112"), value(variable("f112"), true)) :- action(action("add-f113")).
postcondition(action("add-f113"), effect(unconditional), variable("f113"), value(variable("f113"), true)) :- action(action("add-f113")).

action(action("add-f114")).
precondition(action("add-f114"), variable("f113"), value(variable("f113"), true)) :- action(action("add-f114")).
postcondition(action("add-f114"), effect(unconditional), variable("f114"), value(variable("f114"), true)) :- action(action("add-f114")).

action(action("add-f115")).
precondition(action("add-f115"), variable("f114"), value(variable("f114"), true)) :- action(action("add-f115")).
postcondition(action("add-f115"), effect(unconditional), variable("f115"), value(variable("f115"), true)) :- action(action("add-f115")).

action(action("add-f116")).
precondition(action("add-f116"), variable("f115"), value(variable("f115"), true)) :- action(action("add-f116")).
postcondition(action("add-f116"), effect(unconditional), variable("f116"), value(variable("f116"), true)) :- action(action("add-f116")).

action(action("add-f117")).
precondition(action("add-f117"), variable("f116"), value(variable("f116"), true)) :- action(action("add-f117")).
postcondition(action("add-f117"), effect(unconditional), variable("f117"), value(variable("f117"), true)) :- action(action("add-f117")).

action(action("add-f118")).
precondition(action("add-f118"), variable("f117"), value(variable("f117"), true)) :- action(action("add-f118")).
postcondition(action("add-f118"), effect(unconditional), variable("f118"), value(variable("f118"), true)) :- action(action("add-f118")).

action(action("add-f119")).
precondition(action("add-f119"), variable("f118"), value(variable("f118"), true)) :- action(action("add-f119")).
postcondition(action("add-f119"), effect(unconditional), variable("f119"), value(variable("f119"), true)) :- action(action("add-f119")).

action(action("add-f120")).
precondition(action("add-f120"), variable("f119"), value(variable("f119"), true)) :- action(action("add-f120")).
postcondition(action("add-f120"), effect(unconditional), variable("f120"), value(variable("f120"), true)) :- action(action("add-f120")).

action(action("add-f121")).
precondition(action("add-f121"), variable("f120"), value(variable("f120"), true)) :- action(action("add-f121")).
postcondition(action("add-f121"), effect(unconditional), variable("f121"), value(variable("f121"), true)) :- action(action("add-f121")).

action(action("add-f122")).
precondition(action("add-f122"), variable("f121"), value(variable("f121"), true)) :- action(action("add-f122")).
postcondition(action("add-f122"), effect(unconditional), variable("f122"), value(variable("f122"), true)) :- action(action("add-f122")).

action(action("add-f123")).
precondition(action("add-f123"), variable("f122"), value(variable("f122"), true)) :- action(action("add-f123")).
postcondition(action("add-f123"), effect(unconditional), variable("f123"), value(variable("f123"), true)) :- action(action("add-f123")).

action(action("add-f124")).
precondition(action("add-f124"), variable("f123"), value(variable("f123"), true)) :- action(action("add-f124")).
postcondition(action("add-f124"), effect(unconditional), variable("f124"), value(variable("f124"), true)) :- action(action("add-f124")).

action(action("add-f125")).
precondition(action("add-f125"), variable("f124"), value(variable("f124"), true)) :- action(action("add-f125")).
postcondition(action("add-f125"), effect(unconditional), variable("f125"), value(variable("f125"), true)) :- action(action("add-f125")).

action(action("add-f126")).
precondition(action("add-f126"), variable("f125"), value(variable("f125"), true)) :- action(action("add-f126")).
postcondition(action("add-f126"), effect(unconditional), variable("f126"), value(variable("f126"), true)) :- action(action("add-f126")).

action(action("add-f127")).
precondition(action("add-f127"), variable("f126"), value(variable("f126"), true)) :- action(action("add-f127")).
postcondition(action("add-f127"), effect(unconditional), variable("f127"), value(variable("f127"), true)) :- action(action("add-f127")).

action(action("add-f128")).
precondition(action("add-f128"), variable("f127"), value(variable("f127"), true)) :- action(action("add-f128")).
postcondition(action("add-f128"), effect(unconditional), variable("f128"), value(variable("f128"), true)) :- action(action("add-f128")).

action(action("add-f129")).
precondition(action("add-f129"), variable("f128"), value(variable("f128"), true)) :- action(action("add-f129")).
postcondition(action("add-f129"), effect(unconditional), variable("f129"), value(variable("f129"), true)) :- action(action("add-f129")).

action(action("add-f130")).
precondition(action("add-f130"), variable("f129"), value(variable("f129"), true)) :- action(action("add-f130")).
postcondition(action("add-f130"), effect(unconditional), variable("f130"), value(variable("f130"), true)) :- action(action("add-f130")).

action(action("add-f131")).
precondition(action("add-f131"), variable("f130"), value(variable("f130"), true)) :- action(action("add-f131")).
postcondition(action("add-f131"), effect(unconditional), variable("f131"), value(variable("f131"), true)) :- action(action("add-f131")).

action(action("add-f132")).
precondition(action("add-f132"), variable("f131"), value(variable("f131"), true)) :- action(action("add-f132")).
postcondition(action("add-f132"), effect(unconditional), variable("f132"), value(variable("f132"), true)) :- action(action("add-f132")).

action(action("add-f133")).
precondition(action("add-f133"), variable("f132"), value(variable("f132"), true)) :- action(action("add-f133")).
postcondition(action("add-f133"), effect(unconditional), variable("f133"), value(variable("f133"), true)) :- action(action("add-f133")).

action(action("add-f134")).
precondition(action("add-f134"), variable("f133"), value(variable("f133"), true)) :- action(action("add-f134")).
postcondition(action("add-f134"), effect(unconditional), variable("f134"), value(variable("f134"), true)) :- action(action("add-f134")).

action(action("add-f135")).
precondition(action("add-f135"), variable("f134"), value(variable("f134"), true)) :- action(action("add-f135")).
postcondition(action("add-f135"), effect(unconditional), variable("f135"), value(variable("f135"), true)) :- action(action("add-f135")).

action(action("add-f136")).
precondition(action("add-f136"), variable("f135"), value(variable("f135"), true)) :- action(action("add-f136")).
postcondition(action("add-f136"), effect(unconditional), variable("f136"), value(variable("f136"), true)) :- action(action("add-f136")).

action(action("add-f137")).
precondition(action("add-f137"), variable("f136"), value(variable("f136"), true)) :- action(action("add-f137")).
postcondition(action("add-f137"), effect(unconditional), variable("f137"), value(variable("f137"), true)) :- action(action("add-f137")).

action(action("add-f138")).
precondition(action("add-f138"), variable("f137"), value(variable("f137"), true)) :- action(action("add-f138")).
postcondition(action("add-f138"), effect(unconditional), variable("f138"), value(variable("f138"), true)) :- action(action("add-f138")).

action(action("add-f139")).
precondition(action("add-f139"), variable("f138"), value(variable("f138"), true)) :- action(action("add-f139")).
postcondition(action("add-f139"), effect(unconditional), variable("f139"), value(variable("f139"), true)) :- action(action("add-f139")).

action(action("add-f140")).
precondition(action("add-f140"), variable("f139"), value(variable("f139"), true)) :- action(action("add-f140")).
postcondition(action("add-f140"), effect(unconditional), variable("f140"), value(variable("f140"), true)) :- action(action("add-f140")).

action(action("add-f141")).
precondition(action("add-f141"), variable("f140"), value(variable("f140"), true)) :- action(action("add-f141")).
postcondition(action("add-f141"), effect(unconditional), variable("f141"), value(variable("f141"), true)) :- action(action("add-f141")).

action(action("add-f142")).
precondition(action("add-f142"), variable("f141"), value(variable("f141"), true)) :- action(action("add-f142")).
postcondition(action("add-f142"), effect(unconditional), variable("f142"), value(variable("f142"), true)) :- action(action("add-f142")).

action(action("add-f143")).
precondition(action("add-f143"), variable("f142"), value(variable("f142"), true)) :- action(action("add-f143")).
postcondition(action("add-f143"), effect(unconditional), variable("f143"), value(variable("f143"), true)) :- action(action("add-f143")).

action(action("add-f144")).
precondition(action("add-f144"), variable("f143"), value(variable("f143"), true)) :- action(action("add-f144")).
postcondition(action("add-f144"), effect(unconditional), variable("f144"), value(variable("f144"), true)) :- action(action("add-f144")).

action(action("add-f145")).
precondition(action("add-f145"), variable("f144"), value(variable("f144"), true)) :- action(action("add-f145")).
postcondition(action("add-f145"), effect(unconditional), variable("f145"), value(variable("f145"), true)) :- action(action("add-f145")).

action(action("add-f146")).
precondition(action("add-f146"), variable("f145"), value(variable("f145"), true)) :- action(action("add-f146")).
postcondition(action("add-f146"), effect(unconditional), variable("f146"), value(variable("f146"), true)) :- action(action("add-f146")).

action(action("add-f147")).
precondition(action("add-f147"), variable("f146"), value(variable("f146"), true)) :- action(action("add-f147")).
postcondition(action("add-f147"), effect(unconditional), variable("f147"), value(variable("f147"), true)) :- action(action("add-f147")).

action(action("add-f148")).
precondition(action("add-f148"), variable("f147"), value(variable("f147"), true)) :- action(action("add-f148")).
postcondition(action("add-f148"), effect(unconditional), variable("f148"), value(variable("f148"), true)) :- action(action("add-f148")).

action(action("add-f149")).
precondition(action("add-f149"), variable("f148"), value(variable("f148"), true)) :- action(action("add-f149")).
postcondition(action("add-f149"), effect(unconditional), variable("f149"), value(variable("f149"), true)) :- action(action("add-f149")).

action(action("add-f150")).
precondition(action("add-f150"), variable("f149"), value(variable("f149"), true)) :- action(action("add-f150")).
postcondition(action("add-f150"), effect(unconditional), variable("f150"), value(variable("f150"), true)) :- action(action("add-f150")).

action(action("add-f151")).
precondition(action("add-f151"), variable("f150"), value(variable("f150"), true)) :- action(action("add-f151")).
postcondition(action("add-f151"), effect(unconditional), variable("f151"), value(variable("f151"), true)) :- action(action("add-f151")).

action(action("add-f152")).
precondition(action("add-f152"), variable("f151"), value(variable("f151"), true)) :- action(action("add-f152")).
postcondition(action("add-f152"), effect(unconditional), variable("f152"), value(variable("f152"), true)) :- action(action("add-f152")).

action(action("add-f153")).
precondition(action("add-f153"), variable("f152"), value(variable("f152"), true)) :- action(action("add-f153")).
postcondition(action("add-f153"), effect(unconditional), variable("f153"), value(variable("f153"), true)) :- action(action("add-f153")).

action(action("add-f154")).
precondition(action("add-f154"), variable("f153"), value(variable("f153"), true)) :- action(action("add-f154")).
postcondition(action("add-f154"), effect(unconditional), variable("f154"), value(variable("f154"), true)) :- action(action("add-f154")).

action(action("add-f155")).
precondition(action("add-f155"), variable("f154"), value(variable("f154"), true)) :- action(action("add-f155")).
postcondition(action("add-f155"), effect(unconditional), variable("f155"), value(variable("f155"), true)) :- action(action("add-f155")).

action(action("add-f156")).
precondition(action("add-f156"), variable("f155"), value(variable("f155"), true)) :- action(action("add-f156")).
postcondition(action("add-f156"), effect(unconditional), variable("f156"), value(variable("f156"), true)) :- action(action("add-f156")).

action(action("add-f157")).
precondition(action("add-f157"), variable("f156"), value(variable("f156"), true)) :- action(action("add-f157")).
postcondition(action("add-f157"), effect(unconditional), variable("f157"), value(variable("f157"), true)) :- action(action("add-f157")).

action(action("add-f158")).
precondition(action("add-f158"), variable("f157"), value(variable("f157"), true)) :- action(action("add-f158")).
postcondition(action("add-f158"), effect(unconditional), variable("f158"), value(variable("f158"), true)) :- action(action("add-f158")).

action(action("add-f159")).
precondition(action("add-f159"), variable("f158"), value(variable("f158"), true)) :- action(action("add-f159")).
postcondition(action("add-f159"), effect(unconditional), variable("f159"), value(variable("f159"), true)) :- action(action("add-f159")).

action(action("add-f160")).
precondition(action("add-f160"), variable("f159"), value(variable("f159"), true)) :- action(action("add-f160")).
postcondition(action("add-f160"), effect(unconditional), variable("f160"), value(variable("f160"), true)) :- action(action("add-f160")).

action(action("add-f161")).
precondition(action("add-f161"), variable("f160"), value(variable("f160"), true)) :- action(action("add-f161")).
postcondition(action("add-f161"), effect(unconditional), variable("f161"), value(variable("f161"), true)) :- action(action("add-f161")).

action(action("add-f162")).
precondition(action("add-f162"), variable("f161"), value(variable("f161"), true)) :- action(action("add-f162")).
postcondition(action("add-f162"), effect(unconditional), variable("f162"), value(variable("f162"), true)) :- action(action("add-f162")).

action(action("add-f163")).
precondition(action("add-f163"), variable("f162"), value(variable("f162"), true)) :- action(action("add-f163")).
postcondition(action("add-f163"), effect(unconditional), variable("f163"), value(variable("f163"), true)) :- action(action("add-f163")).

action(action("add-f164")).
precondition(action("add-f164"), variable("f163"), value(variable("f163"), true)) :- action(action("add-f164")).
postcondition(action("add-f164"), effect(unconditional), variable("f164"), value(variable("f164"), true)) :- action(action("add-f164")).

action(action("add-f165")).
precondition(action("add-f165"), variable("f164"), value(variable("f164"), true)) :- action(action("add-f165")).
postcondition(action("add-f165"), effect(unconditional), variable("f165"), value(variable("f165"), true)) :- action(action("add-f165")).

action(action("add-f166")).
precondition(action("add-f166"), variable("f165"), value(variable("f165"), true)) :- action(action("add-f166")).
postcondition(action("add-f166"), effect(unconditional), variable("f166"), value(variable("f166"), true)) :- action(action("add-f166")).

action(action("add-f167")).
precondition(action("add-f167"), variable("f166"), value(variable("f166"), true)) :- action(action("add-f167")).
postcondition(action("add-f167"), effect(unconditional), variable("f167"), value(variable("f167"), true)) :- action(action("add-f167")).

action(action("add-f168")).
precondition(action("add-f168"), variable("f167"), value(variable("f167"), true)) :- action(action("add-f168")).
postcondition(action("add-f168"), effect(unconditional), variable("f168"), value(variable("f168"), true)) :- action(action("add-f168")).

action(action("add-f169")).
precondition(action("add-f169"), variable("f168"), value(variable("f168"), true)) :- action(action("add-f169")).
postcondition(action("add-f169"), effect(unconditional), variable("f169"), value(variable("f169"), true)) :- action(action("add-f169")).

action(action("add-f170")).
precondition(action("add-f170"), variable("f169"), value(variable("f169"), true)) :- action(action("add-f170")).
postcondition(action("add-f170"), effect(unconditional), variable("f170"), value(variable("f170"), true)) :- action(action("add-f170")).

action(action("add-f171")).
precondition(action("add-f171"), variable("f170"), value(variable("f170"), true)) :- action(action("add-f171")).
postcondition(action("add-f171"), effect(unconditional), variable("f171"), value(variable("f171"), true)) :- action(action("add-f171")).

action(action("add-f172")).
precondition(action("add-f172"), variable("f171"), value(variable("f171"), true)) :- action(action("add-f172")).
postcondition(action("add-f172"), effect(unconditional), variable("f172"), value(variable("f172"), true)) :- action(action("add-f172")).

action(action("add-f173")).
precondition(action("add-f173"), variable("f172"), value(variable("f172"), true)) :- action(action("add-f173")).
postcondition(action("add-f173"), effect(unconditional), variable("f173"), value(variable("f173"), true)) :- action(action("add-f173")).

action(action("add-f174")).
precondition(action("add-f174"), variable("f173"), value(variable("f173"), true)) :- action(action("add-f174")).
postcondition(action("add-f174"), effect(unconditional), variable("f174"), value(variable("f174"), true)) :- action(action("add-f174")).

action(action("add-f175")).
precondition(action("add-f175"), variable("f174"), value(variable("f174"), true)) :- action(action("add-f175")).
postcondition(action("add-f175"), effect(unconditional), variable("f175"), value(variable("f175"), true)) :- action(action("add-f175")).

action(action("add-f176")).
precondition(action("add-f176"), variable("f175"), value(variable("f175"), true)) :- action(action("add-f176")).
postcondition(action("add-f176"), effect(unconditional), variable("f176"), value(variable("f176"), true)) :- action(action("add-f176")).

action(action("add-f177")).
precondition(action("add-f177"), variable("f176"), value(variable("f176"), true)) :- action(action("add-f177")).
postcondition(action("add-f177"), effect(unconditional), variable("f177"), value(variable("f177"), true)) :- action(action("add-f177")).

action(action("add-f178")).
precondition(action("add-f178"), variable("f177"), value(variable("f177"), true)) :- action(action("add-f178")).
postcondition(action("add-f178"), effect(unconditional), variable("f178"), value(variable("f178"), true)) :- action(action("add-f178")).

action(action("add-f179")).
precondition(action("add-f179"), variable("f178"), value(variable("f178"), true)) :- action(action("add-f179")).
postcondition(action("add-f179"), effect(unconditional), variable("f179"), value(variable("f179"), true)) :- action(action("add-f179")).

action(action("add-f180")).
precondition(action("add-f180"), variable("f179"), value(variable("f179"), true)) :- action(action("add-f180")).
postcondition(action("add-f180"), effect(unconditional), variable("f180"), value(variable("f180"), true)) :- action(action("add-f180")).

action(action("add-f181")).
precondition(action("add-f181"), variable("f180"), value(variable("f180"), true)) :- action(action("add-f181")).
postcondition(action("add-f181"), effect(unconditional), variable("f181"), value(variable("f181"), true)) :- action(action("add-f181")).

action(action("add-f182")).
precondition(action("add-f182"), variable("f181"), value(variable("f181"), true)) :- action(action("add-f182")).
postcondition(action("add-f182"), effect(unconditional), variable("f182"), value(variable("f182"), true)) :- action(action("add-f182")).

action(action("add-f183")).
precondition(action("add-f183"), variable("f182"), value(variable("f182"), true)) :- action(action("add-f183")).
postcondition(action("add-f183"), effect(unconditional), variable("f183"), value(variable("f183"), true)) :- action(action("add-f183")).

action(action("add-f184")).
precondition(action("add-f184"), variable("f183"), value(variable("f183"), true)) :- action(action("add-f184")).
postcondition(action("add-f184"), effect(unconditional), variable("f184"), value(variable("f184"), true)) :- action(action("add-f184")).

action(action("add-f185")).
precondition(action("add-f185"), variable("f184"), value(variable("f184"), true)) :- action(action("add-f185")).
postcondition(action("add-f185"), effect(unconditional), variable("f185"), value(variable("f185"), true)) :- action(action("add-f185")).

action(action("add-f186")).
precondition(action("add-f186"), variable("f185"), value(variable("f185"), true)) :- action(action("add-f186")).
postcondition(action("add-f186"), effect(unconditional), variable("f186"), value(variable("f186"), true)) :- action(action("add-f186")).

action(action("add-f187")).
precondition(action("add-f187"), variable("f186"), value(variable("f186"), true)) :- action(action("add-f187")).
postcondition(action("add-f187"), effect(unconditional), variable("f187"), value(variable("f187"), true)) :- action(action("add-f187")).

action(action("add-f188")).
precondition(action("add-f188"), variable("f187"), value(variable("f187"), true)) :- action(action("add-f188")).
postcondition(action("add-f188"), effect(unconditional), variable("f188"), value(variable("f188"), true)) :- action(action("add-f188")).

action(action("add-f189")).
precondition(action("add-f189"), variable("f188"), value(variable("f188"), true)) :- action(action("add-f189")).
postcondition(action("add-f189"), effect(unconditional), variable("f189"), value(variable("f189"), true)) :- action(action("add-f189")).

action(action("add-f190")).
precondition(action("add-f190"), variable("f189"), value(variable("f189"), true)) :- action(action("add-f190")).
postcondition(action("add-f190"), effect(unconditional), variable("f190"), value(variable("f190"), true)) :- action(action("add-f190")).

action(action("add-f191")).
precondition(action("add-f191"), variable("f190"), value(variable("f190"), true)) :- action(action("add-f191")).
postcondition(action("add-f191"), effect(unconditional), variable("f191"), value(variable("f191"), true)) :- action(action("add-f191")).

action(action("add-f192")).
precondition(action("add-f192"), variable("f191"), value(variable("f191"), true)) :- action(action("add-f192")).
postcondition(action("add-f192"), effect(unconditional), variable("f192"), value(variable("f192"), true)) :- action(action("add-f192")).

action(action("add-f193")).
precondition(action("add-f193"), variable("f192"), value(variable("f192"), true)) :- action(action("add-f193")).
postcondition(action("add-f193"), effect(unconditional), variable("f193"), value(variable("f193"), true)) :- action(action("add-f193")).

action(action("add-f194")).
precondition(action("add-f194"), variable("f193"), value(variable("f193"), true)) :- action(action("add-f194")).
postcondition(action("add-f194"), effect(unconditional), variable("f194"), value(variable("f194"), true)) :- action(action("add-f194")).

action(action("add-f195")).
precondition(action("add-f195"), variable("f194"), value(variable("f194"), true)) :- action(action("add-f195")).
postcondition(action("add-f195"), effect(unconditional), variable("f195"), value(variable("f195"), true)) :- action(action("add-f195")).

action(action("add-f196")).
precondition(action("add-f196"), variable("f195"), value(variable("f195"), true)) :- action(action("add-f196")).
postcondition(action("add-f196"), effect(unconditional), variable("f196"), value(variable("f196"), true)) :- action(action("add-f196")).

action(action("add-f197")).
precondition(action("add-f197"), variable("f196"), value(variable("f196"), true)) :- action(action("add-f197")).
postcondition(action("add-f197"), effect(unconditional), variable("f197"), value(variable("f197"), true)) :- action(action("add-f197")).

action(action("add-f198")).
precondition(action("add-f198"), variable("f197"), value(variable("f197"), true)) :- action(action("add-f198")).
postcondition(action("add-f198"), effect(unconditional), variable("f198"), value(variable("f198"), true)) :- action(action("add-f198")).

action(action("add-f199")).
precondition(action("add-f199"), variable("f198"), value(variable("f198"), true)) :- action(action("add-f199")).
postcondition(action("add-f199"), effect(unconditional), variable("f199"), value(variable("f199"), true)) :- action(action("add-f199")).

action(action("add-f200")).
precondition(action("add-f200"), variable("f199"), value(variable("f199"), true)) :- action(action("add-f200")).
postcondition(action("add-f200"), effect(unconditional), variable("f200"), value(variable("f200"), true)) :- action(action("add-f200")).

action(action("add-f201")).
precondition(action("add-f201"), variable("f200"), value(variable("f200"), true)) :- action(action("add-f201")).
postcondition(action("add-f201"), effect(unconditional), variable("f201"), value(variable("f201"), true)) :- action(action("add-f201")).

action(action("add-f202")).
precondition(action("add-f202"), variable("f201"), value(variable("f201"), true)) :- action(action("add-f202")).
postcondition(action("add-f202"), effect(unconditional), variable("f202"), value(variable("f202"), true)) :- action(action("add-f202")).

action(action("add-f203")).
precondition(action("add-f203"), variable("f202"), value(variable("f202"), true)) :- action(action("add-f203")).
postcondition(action("add-f203"), effect(unconditional), variable("f203"), value(variable("f203"), true)) :- action(action("add-f203")).

action(action("add-f204")).
precondition(action("add-f204"), variable("f203"), value(variable("f203"), true)) :- action(action("add-f204")).
postcondition(action("add-f204"), effect(unconditional), variable("f204"), value(variable("f204"), true)) :- action(action("add-f204")).

action(action("add-f205")).
precondition(action("add-f205"), variable("f204"), value(variable("f204"), true)) :- action(action("add-f205")).
postcondition(action("add-f205"), effect(unconditional), variable("f205"), value(variable("f205"), true)) :- action(action("add-f205")).

action(action("add-f206")).
precondition(action("add-f206"), variable("f205"), value(variable("f205"), true)) :- action(action("add-f206")).
postcondition(action("add-f206"), effect(unconditional), variable("f206"), value(variable("f206"), true)) :- action(action("add-f206")).

action(action("add-f207")).
precondition(action("add-f207"), variable("f206"), value(variable("f206"), true)) :- action(action("add-f207")).
postcondition(action("add-f207"), effect(unconditional), variable("f207"), value(variable("f207"), true)) :- action(action("add-f207")).

action(action("add-f208")).
precondition(action("add-f208"), variable("f207"), value(variable("f207"), true)) :- action(action("add-f208")).
postcondition(action("add-f208"), effect(unconditional), variable("f208"), value(variable("f208"), true)) :- action(action("add-f208")).

action(action("add-f209")).
precondition(action("add-f209"), variable("f208"), value(variable("f208"), true)) :- action(action("add-f209")).
postcondition(action("add-f209"), effect(unconditional), variable("f209"), value(variable("f209"), true)) :- action(action("add-f209")).

action(action("add-f210")).
precondition(action("add-f210"), variable("f209"), value(variable("f209"), true)) :- action(action("add-f210")).
postcondition(action("add-f210"), effect(unconditional), variable("f210"), value(variable("f210"), true)) :- action(action("add-f210")).

action(action("add-f211")).
precondition(action("add-f211"), variable("f210"), value(variable("f210"), true)) :- action(action("add-f211")).
postcondition(action("add-f211"), effect(unconditional), variable("f211"), value(variable("f211"), true)) :- action(action("add-f211")).

action(action("add-f212")).
precondition(action("add-f212"), variable("f211"), value(variable("f211"), true)) :- action(action("add-f212")).
postcondition(action("add-f212"), effect(unconditional), variable("f212"), value(variable("f212"), true)) :- action(action("add-f212")).

action(action("add-f213")).
precondition(action("add-f213"), variable("f212"), value(variable("f212"), true)) :- action(action("add-f213")).
postcondition(action("add-f213"), effect(unconditional), variable("f213"), value(variable("f213"), true)) :- action(action("add-f213")).

action(action("add-f214")).
precondition(action("add-f214"), variable("f213"), value(variable("f213"), true)) :- action(action("add-f214")).
postcondition(action("add-f214"), effect(unconditional), variable("f214"), value(variable("f214"), true)) :- action(action("add-f214")).

action(action("add-f215")).
precondition(action("add-f215"), variable("f214"), value(variable("f214"), true)) :- action(action("add-f215")).
postcondition(action("add-f215"), effect(unconditional), variable("f215"), value(variable("f215"), true)) :- action(action("add-f215")).

action(action("add-f216")).
precondition(action("add-f216"), variable("f215"), value(variable("f215"), true)) :- action(action("add-f216")).
postcondition(action("add-f216"), effect(unconditional), variable("f216"), value(variable("f216"), true)) :- action(action("add-f216")).

action(action("add-f217")).
precondition(action("add-f217"), variable("f216"), value(variable("f216"), true)) :- action(action("add-f217")).
postcondition(action("add-f217"), effect(unconditional), variable("f217"), value(variable("f217"), true)) :- action(action("add-f217")).

action(action("add-f218")).
precondition(action("add-f218"), variable("f217"), value(variable("f217"), true)) :- action(action("add-f218")).
postcondition(action("add-f218"), effect(unconditional), variable("f218"), value(variable("f218"), true)) :- action(action("add-f218")).

action(action("add-f219")).
precondition(action("add-f219"), variable("f218"), value(variable("f218"), true)) :- action(action("add-f219")).
postcondition(action("add-f219"), effect(unconditional), variable("f219"), value(variable("f219"), true)) :- action(action("add-f219")).

action(action("add-f220")).
precondition(action("add-f220"), variable("f219"), value(variable("f219"), true)) :- action(action("add-f220")).
postcondition(action("add-f220"), effect(unconditional), variable("f220"), value(variable("f220"), true)) :- action(action("add-f220")).

action(action("add-f221")).
precondition(action("add-f221"), variable("f220"), value(variable("f220"), true)) :- action(action("add-f221")).
postcondition(action("add-f221"), effect(unconditional), variable("f221"), value(variable("f221"), true)) :- action(action("add-f221")).

action(action("add-f222")).
precondition(action("add-f222"), variable("f221"), value(variable("f221"), true)) :- action(action("add-f222")).
postcondition(action("add-f222"), effect(unconditional), variable("f222"), value(variable("f222"), true)) :- action(action("add-f222")).

action(action("add-f223")).
precondition(action("add-f223"), variable("f222"), value(variable("f222"), true)) :- action(action("add-f223")).
postcondition(action("add-f223"), effect(unconditional), variable("f223"), value(variable("f223"), true)) :- action(action("add-f223")).

action(action("add-f224")).
precondition(action("add-f224"), variable("f223"), value(variable("f223"), true)) :- action(action("add-f224")).
postcondition(action("add-f224"), effect(unconditional), variable("f224"), value(variable("f224"), true)) :- action(action("add-f224")).

action(action("add-f225")).
precondition(action("add-f225"), variable("f224"), value(variable("f224"), true)) :- action(action("add-f225")).
postcondition(action("add-f225"), effect(unconditional), variable("f225"), value(variable("f225"), true)) :- action(action("add-f225")).

action(action("add-f226")).
precondition(action("add-f226"), variable("f225"), value(variable("f225"), true)) :- action(action("add-f226")).
postcondition(action("add-f226"), effect(unconditional), variable("f226"), value(variable("f226"), true)) :- action(action("add-f226")).

action(action("add-f227")).
precondition(action("add-f227"), variable("f226"), value(variable("f226"), true)) :- action(action("add-f227")).
postcondition(action("add-f227"), effect(unconditional), variable("f227"), value(variable("f227"), true)) :- action(action("add-f227")).

action(action("add-f228")).
precondition(action("add-f228"), variable("f227"), value(variable("f227"), true)) :- action(action("add-f228")).
postcondition(action("add-f228"), effect(unconditional), variable("f228"), value(variable("f228"), true)) :- action(action("add-f228")).

action(action("add-f229")).
precondition(action("add-f229"), variable("f228"), value(variable("f228"), true)) :- action(action("add-f229")).
postcondition(action("add-f229"), effect(unconditional), variable("f229"), value(variable("f229"), true)) :- action(action("add-f229")).

action(action("add-f230")).
precondition(action("add-f230"), variable("f229"), value(variable("f229"), true)) :- action(action("add-f230")).
postcondition(action("add-f230"), effect(unconditional), variable("f230"), value(variable("f230"), true)) :- action(action("add-f230")).

action(action("add-f231")).
precondition(action("add-f231"), variable("f230"), value(variable("f230"), true)) :- action(action("add-f231")).
postcondition(action("add-f231"), effect(unconditional), variable("f231"), value(variable("f231"), true)) :- action(action("add-f231")).

action(action("add-f232")).
precondition(action("add-f232"), variable("f231"), value(variable("f231"), true)) :- action(action("add-f232")).
postcondition(action("add-f232"), effect(unconditional), variable("f232"), value(variable("f232"), true)) :- action(action("add-f232")).

action(action("add-f233")).
precondition(action("add-f233"), variable("f232"), value(variable("f232"), true)) :- action(action("add-f233")).
postcondition(action("add-f233"), effect(unconditional), variable("f233"), value(variable("f233"), true)) :- action(action("add-f233")).

action(action("add-f234")).
precondition(action("add-f234"), variable("f233"), value(variable("f233"), true)) :- action(action("add-f234")).
postcondition(action("add-f234"), effect(unconditional), variable("f234"), value(variable("f234"), true)) :- action(action("add-f234")).

action(action("add-f235")).
precondition(action("add-f235"), variable("f234"), value(variable("f234"), true)) :- action(action("add-f235")).
postcondition(action("add-f235"), effect(unconditional), variable("f235"), value(variable("f235"), true)) :- action(action("add-f235")).

action(action("add-f236")).
precondition(action("add-f236"), variable("f235"), value(variable("f235"), true)) :- action(action("add-f236")).
postcondition(action("add-f236"), effect(unconditional), variable("f236"), value(variable("f236"), true)) :- action(action("add-f236")).

action(action("add-f237")).
precondition(action("add-f237"), variable("f236"), value(variable("f236"), true)) :- action(action("add-f237")).
postcondition(action("add-f237"), effect(unconditional), variable("f237"), value(variable("f237"), true)) :- action(action("add-f237")).

action(action("add-f238")).
precondition(action("add-f238"), variable("f237"), value(variable("f237"), true)) :- action(action("add-f238")).
postcondition(action("add-f238"), effect(unconditional), variable("f238"), value(variable("f238"), true)) :- action(action("add-f238")).

action(action("add-f239")).
precondition(action("add-f239"), variable("f238"), value(variable("f238"), true)) :- action(action("add-f239")).
postcondition(action("add-f239"), effect(unconditional), variable("f239"), value(variable("f239"), true)) :- action(action("add-f239")).

action(action("add-f240")).
precondition(action("add-f240"), variable("f239"), value(variable("f239"), true)) :- action(action("add-f240")).
postcondition(action("add-f240"), effect(unconditional), variable("f240"), value(variable("f240"), true)) :- action(action("add-f240")).

horizon(241).
