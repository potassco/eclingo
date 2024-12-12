import unittest

from clingo.ast import Sign
from clingo.symbol import Function

import eclingo as _eclingo
from eclingo.literals import Literal
from eclingo.solver import SolverReification
from eclingo.solver.world_view import EpistemicLiteral, WorldView

# python -m unittest tests.test_project.TestEclingoProject.test_project0


def project(reified_program):
    config = _eclingo.config.AppConfig()
    config.eclingo_semantics = "c19-1"

    # We have no way of testing this, unless we make that parameter part of the configuration.
    # Or we will have to make a call to the generator, tester, and wv_builder one by one to access the
    # control value of the generator.

    solver = SolverReification(reified_program, config)

    wviews = []
    for model in solver.solve():
        # if model not in wviews:
        # This line obviously solves the problem, but just because does not append equals
        wviews.append(model)
    return sorted(wviews)


class TestCase(unittest.TestCase):
    def assert_models(self, models, expected):
        self.assertEqual(models, expected)


class TestEclingoProject(TestCase):
    # Given auto,3 as project parameter should not give 2 world views.
    def test_project0(self):
        self.maxDiff = None
        # echo "b :- &k{ not a }. c :- &k{ b }. {a}." | eclingo --semantics c19-1 --reification
        self.assert_models(
            project(
                """tag(incremental). atom_tuple(0). atom_tuple(0,1). literal_tuple(0).
                                   rule(choice(0),normal(0)). atom_tuple(1). atom_tuple(1,2). literal_tuple(1).
                                   literal_tuple(1,-1). rule(disjunction(1),normal(1)). atom_tuple(2). atom_tuple(2,3). literal_tuple(2).
                                   literal_tuple(2,2). rule(choice(2),normal(2)). atom_tuple(3). atom_tuple(3,4). literal_tuple(3).
                                   literal_tuple(3,3). rule(disjunction(3),normal(3)). output(k(not1(u(b))),3). literal_tuple(4).
                                   literal_tuple(4,1). output(u(b),4). literal_tuple(5). literal_tuple(5,4). output(u(a),5).
                                   output(not1(u(b)),2). rule(choice(0),normal(0)). rule(disjunction(1),normal(1)).
                                   rule(choice(2),normal(2)). rule(disjunction(3),normal(3))."""
            ),
            [
                WorldView(
                    [
                        EpistemicLiteral(
                            Literal(Function("b", [], True), Sign.NoSign), 0, True
                        )
                    ]
                ),
            ],
        )
