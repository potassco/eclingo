import unittest

from clingo.ast import Sign
from clingo.symbol import Function

import eclingo as _eclingo
from eclingo.literals import Literal
from eclingo.solver import SolverReification
from eclingo.solver.world_view import EpistemicLiteral, WorldView

from tests.parse_programs import parse_program

# python -m unittest tests.test_solver_reification.TestEclingoSolverReification.test_solver_reification01

""" SOLVER for test_solver """


def solve(reified_program):
    reified_program = parse_program(reified_program)
    config = _eclingo.config.AppConfig()
    config.eclingo_semantics = "c19-1"

    solver = SolverReification(reified_program, config)

    wviews = []
    for model in solver.solve():
        # if model not in wviews:
        wviews.append(model)
    return sorted(wviews)
    # return wviews


class TestCase(unittest.TestCase):
    def assert_models(self, models, expected):
        self.assertEqual(models, expected)


class TestEclingoSolverReification(TestCase):
    def test_solver_reification01(self):
        # echo "a. b :- &k{a}." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0).
                                    rule(disjunction(0),normal(0)). atom_tuple(1).
                                    atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2).
                                    atom_tuple(2,3). literal_tuple(1). literal_tuple(1,2).
                                    rule(disjunction(2),normal(1)). output(k(u(a)),1).
                                    output(u(a),0). literal_tuple(2). literal_tuple(2,3). output(u(b),2)."""
            ),
            [WorldView([EpistemicLiteral(Function("a", [], True), 0, False)])],
        )

    def test_solver_reification_explicit_negation(self):
        # echo "-a. b :- &k{-a}. c :- &k{b}." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
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
                                    rule(disjunction(4),normal(3))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(Function("b", [], True), Sign.NoSign, False),
                        EpistemicLiteral(Function("a", [], False), 0, False),
                    ]
                )
            ],
        )

    def test_solver_reification_double_negation(self):
        # echo "a. b :- &k{ not not a }." | eclingo --output=reify --semantics c19-1 --reification
        self.assert_models(
            solve(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                        atom_tuple(1). atom_tuple(1,2). rule(disjunction(1),normal(0)). atom_tuple(2). atom_tuple(2,3).
                        rule(choice(2),normal(0)). atom_tuple(3). atom_tuple(3,4). literal_tuple(1). literal_tuple(1,3).
                        rule(disjunction(3),normal(1)). output(k(not2(u(a))),1). output(u(a),0). literal_tuple(2).
                        literal_tuple(2,4). output(u(b),2). output(not2(u(a)),0). rule(choice(2),normal(0)).
                        rule(disjunction(3),normal(1))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("a", [], True), Sign.DoubleNegation),
                            0,
                            False,
                        )
                    ]
                )
            ],
        )

    def test_solver_reification02(self):
        # echo "{a}. :- not a. b :- &k{a}. c :- &k{b}." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
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
                                         rule(choice(3),normal(3)). rule(disjunction(4),normal(4)). rule(disjunction(5),normal(5))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(Function("a", [], True), Sign.NoSign, False),
                        EpistemicLiteral(Function("b", [], True), Sign.NoSign, False),
                    ]
                )
            ],
        )

    def test_solver_reification03(self):
        # echo "-a. b:- &k{-a}. c :- b." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                    atom_tuple(1). atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2). atom_tuple(2,3).
                    literal_tuple(1). literal_tuple(1,2). rule(disjunction(2),normal(1)). atom_tuple(3). atom_tuple(3,4).
                    literal_tuple(2). literal_tuple(2,3). rule(disjunction(3),normal(2)). output(k(u(-a)),1).
                    output(u(-a),0). output(u(b),2). literal_tuple(3). literal_tuple(3,4). output(u(c),3).
                    rule(choice(1),normal(0)). rule(disjunction(2),normal(1)). rule(disjunction(3),normal(2))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("a", [], False), Sign.NoSign), 0, False
                        )
                    ]
                )
            ],
        )

    def test_solver_reification04(self):
        # echo "-a. b :- &k{-a}." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
                """atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)). atom_tuple(1).
                    atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2). atom_tuple(2,3). literal_tuple(1).
                    literal_tuple(1,2). rule(disjunction(2),normal(1)). output(k(u(-a)),1). output(u(-a),0). literal_tuple(2).
                    literal_tuple(2,3). output(u(b),2)."""
            ),
            [WorldView([EpistemicLiteral(Function("a", [], False), 0, False)])],
        )

    def test_solver_reification_negation(self):
        # echo "b :- &k{ not a }. c :- &k{ b }." | eclingo --semantics c19-1 --reification
        self.assert_models(
            solve(
                """atom_tuple(0). atom_tuple(0,1). literal_tuple(0). rule(disjunction(0),normal(0)).
                                 atom_tuple(1). atom_tuple(1,2). rule(choice(1),normal(0)). atom_tuple(2).
                                 atom_tuple(2,3). literal_tuple(1). literal_tuple(1,2). rule(disjunction(2),normal(1)).
                                 atom_tuple(3). atom_tuple(3,4). literal_tuple(2). literal_tuple(2,3). rule(choice(3),normal(2)).
                                 atom_tuple(4). atom_tuple(4,5). literal_tuple(3). literal_tuple(3,4). rule(disjunction(4),normal(3)).
                                 output(k(not1(u(a))),1). output(k(u(b)),3). output(u(b),2). literal_tuple(4).
                                 literal_tuple(4,5). output(u(c),4). output(not1(u(a)),0). rule(choice(1),normal(0)).
                                 rule(disjunction(2),normal(1)). rule(choice(3),normal(2)). rule(disjunction(4),normal(3))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("b", [], True), Sign.NoSign), 0, is_m=False
                        ),
                    ]
                )
            ],
        )

    def test_solver_reification_no_facts(self):
        # echo "a :- not &k{ b }. b :- not &k{ a }." |eclingo --semantics=19-1 --reification
        self.assert_models(
            solve(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0). literal_tuple(0,-2). rule(disjunction(0),normal(0)).
                atom_tuple(1). atom_tuple(1,3). literal_tuple(1). literal_tuple(1,1). rule(choice(1),normal(1)).
                atom_tuple(2). atom_tuple(2,4). literal_tuple(2). literal_tuple(2,-3). rule(disjunction(2),normal(2)).
                atom_tuple(3). atom_tuple(3,2). literal_tuple(3). literal_tuple(3,4). rule(choice(3),normal(3)).
                literal_tuple(4). literal_tuple(4,2). output(k(u(b)),4). literal_tuple(5). literal_tuple(5,3).
                output(k(u(a)),5). output(u(a),1). output(u(b),3). rule(disjunction(0),normal(0)). rule(choice(1),normal(1)).
                rule(disjunction(2),normal(2)). rule(choice(3),normal(3))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("a", [], True), Sign.NoSign), 0, is_m=False
                        ),
                    ]
                ),
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("b", [], True), Sign.NoSign), 0, is_m=False
                        ),
                    ]
                ),
            ],
        )
