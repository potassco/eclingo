import unittest

from clingo.symbol import Function

import eclingo as _eclingo
from eclingo.solver.candidate import Candidate
from eclingo.solver.tester import CandidateTesterReification

from tests.parse_programs import parse_program

# python -m unittest tests.test_tester_reification.TestEclingoTesterReification

""" Helper function to generate candidates for a given program and test them"""


def tester(program, candidates):
    program = parse_program(program)
    config = _eclingo.config.AppConfig()
    config.eclingo_semantics = "c19-1"

    test_candidate = CandidateTesterReification(config, program)
    tested = []
    for candidate in candidates:
        if test_candidate(candidate):
            if candidate not in tested:
                tested.append(candidate)

    return sorted(tested)


class TestCase(unittest.TestCase):
    def assert_models(self, candidates, expected):
        self.assertEqual(candidates, expected)


class TestEclingoTesterReification(TestCase):
    def test_tester_reification(self):
        # echo ":- k(u(a)). u(a). {k(u(a))} :- u(a)." | clingo --output=reify
        # "a. b :- &k{a}."
        self.assert_models(
            tester(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0).
                                    rule(disjunction(0),normal(0)). atom_tuple(1).
                                    atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2).
                                    atom_tuple(2,3). literal_tuple(1). literal_tuple(1,2).
                                    rule(disjunction(2),normal(1)). output(k(u(a)),1).
                                    output(u(a),0). literal_tuple(2). literal_tuple(2,3). output(u(b),2).""",
                [
                    Candidate(
                        pos=[],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], True)], True)],
                                True,
                            )
                        ],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], True)], True)],
                                True,
                            )
                        ],
                        neg=[],
                    ),
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k", [Function("u", [Function("a", [], True)], True)], True
                        )
                    ],
                    neg=[],
                )
            ],
        )

    def test_tester_reification_double_negation(self):
        # echo "a. b :- &k{ not not a }." | eclingo --output=reify --semantics c19-1 --reification
        self.assert_models(
            tester(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                        atom_tuple(1). atom_tuple(1,2). rule(disjunction(1),normal(0)). atom_tuple(2). atom_tuple(2,3).
                        rule(choice(2),normal(0)). atom_tuple(3). atom_tuple(3,4). literal_tuple(1). literal_tuple(1,3).
                        rule(disjunction(3),normal(1)). output(k(not2(u(a))),1). output(u(a),0). literal_tuple(2).
                        literal_tuple(2,4). output(u(b),2). output(not2(u(a)),0). rule(choice(2),normal(0)).
                        rule(disjunction(3),normal(1)).""",
                [
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [
                                    Function(
                                        "not2",
                                        [
                                            Function(
                                                "u", [Function("a", [], True)], True
                                            )
                                        ],
                                        True,
                                    )
                                ],
                                True,
                            )
                        ],
                        neg=[],
                    )
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k",
                            [
                                Function(
                                    "not2",
                                    [Function("u", [Function("a", [], True)], True)],
                                    True,
                                )
                            ],
                            True,
                        )
                    ],
                    neg=[],
                )
            ],
        )

    def test_tester_reification_explicit_negation(self):
        # echo "-a. b:- &k{-a}. c :- b." | eclingo --semantics c19-1 --reification --output=reify
        self.assert_models(
            tester(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                    atom_tuple(1). atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2). atom_tuple(2,3).
                    literal_tuple(1). literal_tuple(1,2). rule(disjunction(2),normal(1)). atom_tuple(3). atom_tuple(3,4).
                    literal_tuple(2). literal_tuple(2,3). rule(disjunction(3),normal(2)). output(k(u(-a)),1).
                    output(u(-a),0). output(u(b),2). literal_tuple(3). literal_tuple(3,4). output(u(c),3).
                    rule(choice(1),normal(0)). rule(disjunction(2),normal(1)). rule(disjunction(3),normal(2)).""",
                [
                    Candidate(
                        pos=[],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            )
                        ],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            )
                        ],
                        neg=[],
                    ),
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k", [Function("u", [Function("a", [], False)], True)], True
                        )
                    ],
                    neg=[],
                )
            ],
        )

    def test_tester_reification_explicit_negation02(self):
        # echo "u(-a). u(b) :- k(u(-a)). {k(u(-a))}." | clingo --output=reify
        # echo "-a. b :- &k{-a}." | eclingo --semantics c19-1 --reification --output=reify
        self.assert_models(
            tester(
                """atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)). atom_tuple(1).
                    atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2). atom_tuple(2,3). literal_tuple(1).
                    literal_tuple(1,2). rule(disjunction(2),normal(1)). output(k(u(-a)),1). output(u(-a),0). literal_tuple(2).
                    literal_tuple(2,3). output(u(b),2).""",
                [
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            )
                        ],
                        neg=[],
                    )
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k", [Function("u", [Function("a", [], False)], True)], True
                        )
                    ],
                    neg=[],
                )
            ],
        )

    def test_tester_reification_explicit_negation03(self):
        self.maxDiff = None
        # echo "-a. b :- &k{-a}. c :- &k{b}." | eclingo --semantics c19-1 --reification --output=reify
        self.assert_models(
            tester(
                """tag(incremental).
                                    atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                                    atom_tuple(1). atom_tuple(1,2). rule(choice(1),normal(0)).
                                    atom_tuple(2). atom_tuple(2,3). literal_tuple(1).
                                    literal_tuple(1,2). rule(disjunction(2),normal(1)). atom_tuple(3).
                                    atom_tuple(3,4). literal_tuple(2). literal_tuple(2,3). rule(choice(3),normal(2)).
                                    atom_tuple(4). atom_tuple(4,5). literal_tuple(3). literal_tuple(3,4).
                                    rule(disjunction(4),normal(3)). output(k(u(-a)),1). output(k(u(b)),3). output(u(-a),0).
                                    output(u(b),2). literal_tuple(4). literal_tuple(4,5). output(u(c),4).
                                    rule(choice(1),normal(0)). rule(disjunction(2),normal(1)). rule(choice(3),normal(2)).
                                    rule(disjunction(4),normal(3)).""",
                [
                    Candidate(
                        pos=[],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            ),
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            ),
                        ],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            ),
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            ),
                        ],
                        neg=[],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], False)], True)],
                                True,
                            )
                        ],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            )
                        ],
                    ),
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k", [Function("u", [Function("b", [], True)], True)], True
                        ),
                        Function(
                            "k", [Function("u", [Function("a", [], False)], True)], True
                        ),
                    ],
                    neg=[],
                ),
            ],
        )

    def test_tester_reification_default_negation02(self):
        self.maxDiff = None
        # echo "{a}. :- not a. b :- &k{a}. c :- &k{b}." | eclingo --semantics c19-1 --reification --output=reify
        self.assert_models(
            tester(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0).
                                         rule(choice(0),normal(0)). atom_tuple(1). atom_tuple(1,2). literal_tuple(1).
                                         literal_tuple(1,1). rule(choice(1),normal(1)). atom_tuple(2). atom_tuple(2,3).
                                         literal_tuple(2). literal_tuple(2,2). rule(disjunction(2),normal(2)). atom_tuple(3).
                                         atom_tuple(3,4). literal_tuple(3). literal_tuple(3,3). rule(choice(3),normal(3)).
                                         atom_tuple(4). atom_tuple(4,5). literal_tuple(4). literal_tuple(4,4).
                                         rule(disjunction(4),normal(4)). atom_tuple(5). literal_tuple(5). literal_tuple(5,-1).
                                         rule(disjunction(5),normal(5)). output(u(a),1). output(u(b),3). literal_tuple(6).
                                         literal_tuple(6,5). output(u(c),6). output(k(u(a)),2). output(k(u(b)),4).
                                         rule(choice(0),normal(0)). rule(choice(1),normal(1)). rule(disjunction(2),normal(2)).
                                         rule(choice(3),normal(3)). rule(disjunction(4),normal(4)). rule(disjunction(5),normal(5)).""",
                [
                    Candidate(
                        pos=[],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], True)], True)],
                                True,
                            ),
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            ),
                        ],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], True)], True)],
                                True,
                            )
                        ],
                        neg=[
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            )
                        ],
                    ),
                    Candidate(
                        pos=[
                            Function(
                                "k",
                                [Function("u", [Function("a", [], True)], True)],
                                True,
                            ),
                            Function(
                                "k",
                                [Function("u", [Function("b", [], True)], True)],
                                True,
                            ),
                        ],
                        neg=[],
                    ),
                ],
            ),
            [
                Candidate(
                    pos=[
                        Function(
                            "k", [Function("u", [Function("a", [], True)], True)], True
                        ),
                        Function(
                            "k", [Function("u", [Function("b", [], True)], True)], True
                        ),
                    ],
                    neg=[],
                )
            ],
        )
