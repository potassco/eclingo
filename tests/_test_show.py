from clingo import Function

from helper_test.helper_parsing import ParsingTestHelper
from helper_test.helper_wv_builder_show import WorldWiewBuilderWithShowTestHelper

# python -m unittest tests.test_show.Test.test_show10_positive_programs


class Test(ParsingTestHelper, WorldWiewBuilderWithShowTestHelper):
    def setUp(self):
        super().setUp()

    def test_show01(self):
        self.assert_equal_show_program(
            "a.  #show a/0.",
            [Function("show_statement", [Function("a", [], True)], True)],
        )

    def test_show02(self):
        self.assert_equal_show_program(
            "{b}.  #show b/0.",
            [Function("show_statement", [Function("b", [], True)], True)],
        )

    def test_show03(self):
        self.assert_equal_show_program("b. b :- &k{a}.", [])

    def test_show04(self):
        self.assert_equal_show_program(
            "b. b :- &k{a}. a. #show b/0. #show a/0.",
            [
                Function("show_statement", [Function("b", [], True)], True),
                Function("show_statement", [Function("a", [], True)], True),
            ],
        )

    def test_show07(self):
        self.assert_equal_world_views(
            "{a}. :- not a. b :- &k{a}. c :- not &k{ not a }.", [["&k{a}"]]
        )

    def test_show08(self):
        self.assert_equal_world_views("a :-  &k{a}. a. #show a/0.", [["&k{a}"]])

    def test_show09(self):
        self.assert_equal_world_views("-a :- &k{-a}. -a. #show -a/0.", [["&k{-a}"]])

    def test_show10_positive_programs(self):
        self.assert_equal_world_views(
            "a. b :- &k{a}. #show a/0. #show b/0.", [["&k{a}"]]
        )
        self.assert_equal_world_views(
            """
            a :- not c.
            c :- not a.
            b :- &k{ not a }.
            :- b.
            #show a/0. #show b/0.
            """,
            [["&m{a}"]],
        )

        self.assert_equal_world_views(
            "{a}. :- not a. b :- &k{a}. #show a/0. #show b/0.",
            [["&k{a}"]],
        )
        self.assert_equal_world_views(
            """
            a :- not &k{ not a}.
            b :- a.
            c :- &k{b}.
            d :- &k{c}.
            #show a/0. #show b/0. #show c/0.""",
            [[], ["&m{a}", "&k{b}", "&k{c}"]],
        )
        self.assert_equal_world_views(
            "{a}. :- not a. b :- &k{a}. c :- &k{b}. #show a/0. #show b/0. #show c/0.",
            [["&k{a}", "&k{b}"]],
        )

    def test_show11_programs_with_strong_negation(self):
        self.assert_equal_world_views(
            "-a. b :- &k{-a}. #show -a/0. #show b/0.", [["&k{-a}"]]
        )
        self.assert_equal_world_views(
            """-a :- not c.
            c :- not -a.
            b :- &k{ not -a }.
            :- b.
            #show a/0. #show -a/0. #show b/0.""",
            [["&m{-a}"]],
        )
        self.assert_equal_world_views(
            "{-a}. :- not -a. b :- &k{-a}. #show -a/0. #show b/0.",
            [["&k{-a}"]],
        )
        self.assert_equal_world_views(
            """
            -a :- not &k{ not -a}.
            b :- -a.
            c :- &k{b}.
            d :- &k{c}.
            #show a/0. #show b/0. #show c/0.""",
            [[], ["&k{b}", "&k{c}"]],
        )
        self.assert_equal_world_views(
            "{-a}. :- not -a. b :- &k{-a}. c :- &k{b}. #show -a/0. #show b/0. #show c/0.",
            [["&k{b}"]],
        )

    def test_show12_programs_with_default_negation(self):
        self.assert_equal_world_views(
            "a. b :- &k{ not not a }. #show a/0. #show b/0.", [["&k{not not a}"]]
        )
        self.assert_equal_world_views(
            "a. b :- &k{ not not a }.  #show b/0.",
            [["&k{not not a}"]],
        )
        self.assert_equal_world_views(
            "b :- &k{ not a }. c :- &k{ b }. #show a/0. #show b/0. #show c/0.",
            [["&k{b}"]],
        )
        self.assert_equal_world_views(
            "b :- &k{ not not a }. c :- &k{ b }. #show a/0. #show b/0. #show c/0.",
            [[]],
        )
        self.assert_equal_world_views(
            """
            a :- not c.
            c :- not a.
            b :- &k{ not a }.
            :- b.
            #show a/0.
            #show b/0.
            #show c/0.
            """,
            [["&m{a}"]],
        )
        self.assert_equal_world_views(
            """
            a :- not c.
            c :- not a.
            b :- not &k{ not a }.
            d :- &k{ b }.
            #show a/0.
            #show b/0.
            #show c/0.
            """,
            [["&k{b}", "&m{a}"]],
        )
        self.assert_equal_world_views(
            """
            a, c.
            b :- not &k{ not a }.
            d :- &k{ b }.
            #show a/0.
            #show b/0.
            #show c/0.
            """,
            [["&k{b}", "&m{a}"]],
        )

    def test_show13_non_ground_programs(self):
        self.assert_equal_world_views("a(1). #show a/1.", [[]])
        self.assert_equal_world_views(
            "a(1). b(X) :- &k{a(X)}. #show a/1. #show b/1.",
            [["&k{a(1)}"]],
        )
        self.assert_equal_world_views(
            "{a(1)}. b(X) :- &k{a(X)}. #show a/1. #show b/1.",
            [[]],
        )
        self.assert_equal_world_views(
            "{a(1)}. :- not a(1). b(X) :- &k{a(X)}. #show a/1. #show b/1.",
            [["&k{a(1)}"]],
        )
        self.assert_equal_world_views(
            """a(1).
            b(X) :- &k{a(X)}.
            c(X) :- &k{b(X)}.
            #show a/1.
            #show b/1.
            #show c/1.""",
            [["&k{b(1)}"]],
        )
        self.assert_equal_world_views(
            """
            {a(1)}.
            :- not a(1).
            b(X) :- &k{a(X)}.
            c(X) :- &k{b(X)}.
            #show a/1.
            #show b/1.
            #show c/1.""",
            [["&k{a(1)}", "&k{b(1)}"]],
        )
        self.assert_equal_world_views(
            "-a(1). b(X) :- &k{-a(X)}. #show -a/1. #show b/1.",
            [["&k{-a(1)}"]],
        )
        self.assert_equal_world_views(
            "{-a(1)}. b(X) :- &k{-a(X)}. #show -a/1. #show b/1.",
            [[]],
        )
        self.assert_equal_world_views(
            "{-a(1)}. :- not -a(1). b(X) :- &k{-a(X)}. #show -a/1. #show b/1.",
            [["&k{-a(1)}"]],
        )
        self.assert_equal_world_views(
            """
            {-a(1)}.
            :- not -a(1).
            b(X) :- &k{-a(X)}.
            c(X) :- &k{b(X)}.
            #show -a/1.
            #show b/1.
            #show c/1.""",
            [["&k{b(1)}"]],
        )

    def test_show14_non_ground_programs_with_default_negation(self):
        self.assert_equal_world_views(
            """
            a(1).
            b(X) :- &k{ not not a(X) }, dom(X).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            """,
            [["&k{not not a(1)}"]],
        )
        self.assert_equal_world_views(
            """
            b(X) :- &k{ not a(X) }, dom(X).
            c(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            """,
            [["&k{b(1)}", "&k{b(2)}"]],
        )
        self.assert_equal_world_views(
            """
            b(X) :- &k{ not not a(X) }, dom(X).
            c(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            """,
            [[]],
        )
        self.assert_equal_world_views(
            """
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- &k{ not a(X) }, dom(X).
            :- b(1).
            :- not b(2).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            """,
            [["&m{a(1)}"]],
        )
        self.assert_equal_world_views(
            """
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            d(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            """,
            [["&k{b(1)}", "&m{a(1)}"]],
        )
        self.assert_equal_world_views(
            """
            a(1), c(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            d(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            #show d/1.
            """,
            [["&k{b(1)}", "&m{a(1)}"]],
        )

    def test_show15_planning(self):
        self.assert_equal_world_views(
            """
            occurs(pull_trigger,0).
            b :- &k{occurs(pull_trigger,0)}.
            #show occurs/2.
            """,
            [["&k{occurs(pull_trigger,0)}"]],
        )
