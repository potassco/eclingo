from clingo import ast as _ast

from eclingo.util.groundprogram import *
from eclingo.internal_states import ShowStatement
from helper_test import helper as _helpler
from helper_test.helper_clingo import ClingoTestHelper
from helper_test.helper_parsing import ParsingTestHelper
from helper_test.helper_wv_builder_show import \
    WorldWiewBuilderWithShowTestHelper


class Test(ClingoTestHelper,
           ParsingTestHelper,
           WorldWiewBuilderWithShowTestHelper):

    def setUp(self):
        super().setUp()
        self.printing = False
        self.printing_ast_repr = False

    def test_01a(self):
        program = """
            #show a/0.
            """
        parsed_program = [
            _ast.Program( # pylint: disable=no-member
                location = {'begin': {'filename': '<string>', 'line': 1, 'column': 1}, 'end': {'filename': '<string>', 'line': 1, 'column': 1}},
                name = 'base',
                parameters = []
                ),
            _ast.ShowSignature( # pylint: disable=no-member
                location = {'begin': {'filename': '<string>', 'line': 2, 'column': 13}, 'end': {'filename': '<string>', 'line': 2, 'column': 23}},
                name = 'a',
                arity = 0,
                positive = True,
                csp = False
            )]
        self.assert_equal_clingo_parsed_program(program, parsed_program)

    def test_show01b(self):
        program = """
            {a}.
            {b}.
            #show a/0.
            """
        ground_program = [
            ClingoOutputAtom(symbol=_helpler.a, atom=2, order=0),
            ClingoRule(choice=True, head=[1], body=[], order=1),
            ClingoRule(choice=True, head=[2], body=[], order=1)
        ]
        ground_program.sort()
        self.assert_equal_clingo_ground_program(program, ground_program)

    def test_show01c(self):
        self.assert_equal_parsing_program_with_show("a. b. #show a/0.", "u_a. u_b.", [ShowStatement(name='a', arity=0, poistive=True)])


    def test_show02(self):
        program = """
            #show -a/0.
            """
        parsed_program = [
            _ast.Program(    # pylint: disable=no-member
                location = {'begin': {'filename': '<string>', 'line': 1, 'column': 1}, 'end': {'filename': '<string>', 'line': 1, 'column': 1}},
                name = 'base',
                parameters = []
                ),
            _ast.ShowSignature(    # pylint: disable=no-member
                location = {'begin': {'filename': '<string>', 'line': 2, 'column': 13}, 'end': {'filename': '<string>', 'line': 2, 'column': 23}},
                name = 'a',
                arity = 0,
                positive = False,
                csp = False
            )]
        self.assert_equal_clingo_parsed_program(program, parsed_program)


    def test_show02b(self):
        program = """
            {-a}.
            {b}.
            #show -a/0.
            """
        ground_program = [
            ClingoOutputAtom(symbol=_helpler.s_neg(_helpler.a), atom=2, order=0),
            ClingoRule(choice=True, head=[1], body=[], order=1),
            ClingoRule(choice=True, head=[2], body=[], order=1)
        ]
        ground_program.sort()
        self.assert_equal_clingo_ground_program(program, ground_program)

    def test_show02c(self):
        self.assert_equal_parsing_program_with_show("-a. b. #show -a/0.", "-u_a. u_b.", [ShowStatement(name='a', arity=0, poistive=False)])

    def test_show03_not_supported(self):
        with self.assertRaises(RuntimeError) as contex_manager:
            self.parse_program("a. b. #show a(0).")
        self.assertEqual(contex_manager.exception.args[0], 'syntax error: only show statements of the form "#show atom/n." are allowed.')

    def test_show04(self):
        self.assert_equal_parsing_program_with_show("a. #show a/0.", "u_a.", [ShowStatement(name='a', arity=0, poistive=True)])

    def test_show05(self):
        self.assert_equal_show_symbols('a.  #show a/0.', ['u_a'])

    def test_show05b(self):
        self.assert_equal_show_symbols('a. b.  #show a/0.', ['u_a'])

    def test_show05c(self):
        self.assert_equal_show_symbols('-a. b.  #show -a/0.', ['-u_a'])

    def test_show05d(self):
        self.assert_equal_show_symbols('#show a/0.', [])

    def test_show06(self):
        self.assert_equal_show_program('a.  #show a/0.', ['u_a.'])

    def test_show06b(self):
        self.assert_equal_show_program('{a}.  #show a/0.', ['{u_a}.', 'not_u_a :- not u_a.'])

    def test_show06c(self):
        self.assert_equal_show_program('#show a/0.', [])

    def test_show07(self):
        self.assert_equal_world_views(self.solve('{a}. :- not a. b :- &k{a}. c :- not &k{ not a }.'), [['&k{a}']])
        
    def test_show08(self):
        self.assert_equal_world_views(self.solve('a.  #show a/0.'), [['&k{a}']])

    def test_show09(self):
        self.assert_equal_world_views(self.solve('-a.  #show -a/0.'), [['&k{-a}']])

    def test_show10_positive_programs(self):
        self.assert_equal_world_views(self.solve('a. b :- &k{a}. #show a/0. #show b/0.'), [['&k{a}', '&k{b}']])
        self.assert_equal_world_views(self.solve('{a}. b :- &k{a}. #show a/0. #show b/0.'), [['&m{a}']])
        self.assert_equal_world_views(self.solve('{a}. :- not a. b :- &k{a}. #show a/0. #show b/0.'), [['&k{a}', '&k{b}']])
        self.assert_equal_world_views(self.solve('a. b :- &k{a}. c :- &k{b}. #show a/0. #show b/0. #show c/0.'), [['&k{a}', '&k{b}', '&k{c}']])
        self.assert_equal_world_views(self.solve('{a}. :- not a. b :- &k{a}. c :- &k{b}. #show a/0. #show b/0. #show c/0.'), [['&k{a}', '&k{b}', '&k{c}']])

    def test_show11_programs_with_strong_negation(self):
        self.assert_equal_world_views(self.solve('-a. b :- &k{-a}. #show -a/0. #show b/0.'), [['&k{-a}', '&k{b}']])
        self.assert_equal_world_views(self.solve('{-a}. b :- &k{-a}. #show -a/0. #show b/0.'), [['&m{-a}']])
        self.assert_equal_world_views(self.solve('{-a}. :- not -a. b :- &k{-a}. #show -a/0. #show b/0.'), [['&k{-a}', '&k{b}']])
        self.assert_equal_world_views(self.solve('-a. b :- &k{-a}. c :- &k{b}. #show -a/0. #show b/0. #show c/0.'), [['&k{-a}', '&k{b}', '&k{c}']])
        self.assert_equal_world_views(self.solve('{-a}. :- not -a. b :- &k{-a}. c :- &k{b}. #show -a/0. #show b/0. #show c/0.'), [['&k{-a}', '&k{b}', '&k{c}']])

    def test_show12_programs_with_default_negation(self):
        self.assert_equal_world_views(self.solve('a. b :- &k{ not a }. #show a/0. #show b/0.'), [['&k{a}']])
        self.assert_equal_world_views(self.solve('a. b :- &k{ not not a }. #show a/0. #show b/0.'), [['&k{a}', '&k{b}']])
        self.assert_equal_world_views(self.solve('b :- &k{ not a }. c :- &k{ b }.  #show a/0. #show b/0. #show c/0.'), [['&k{b}', '&k{c}']])
        self.assert_equal_world_views(self.solve('b :- &k{ not not a }. c :- &k{ b }. #show a/0. #show b/0. #show c/0.'), [[]])
        self.assert_equal_world_views(self.solve('''
            a :- not c.
            c :- not a.
            b :- &k{ a }.
            :- b.
            #show a/0.
            #show b/0.
            #show c/0.
            '''), [['&m{a}', '&m{c}']])
        self.assert_equal_world_views(self.solve('''
            a :- not c.
            c :- not a.
            b :- &k{ not a }.
            :- b.
            #show a/0.
            #show b/0.
            #show c/0.
            '''), [['&m{a}', '&m{c}']])
        self.assert_equal_world_views(self.solve('''
            a :- not c.
            c :- not a.
            b :- not &k{ not a }.
            d :- &k{ b }.
            #show a/0.
            #show b/0.
            #show c/0.
            '''), [['&k{b}', '&m{a}', '&m{c}']])
        self.assert_equal_world_views(self.solve('''
            a, c.
            b :- not &k{ not a }.
            d :- &k{ b }.
            #show a/0.
            #show b/0.
            #show c/0.
            '''), [['&k{b}', '&m{a}', '&m{c}']])

    def test_show13_non_ground_programs(self):
        self.assert_equal_world_views(self.solve('a(1). #show a/1.'), [['&k{a(1)}']])
        self.assert_equal_world_views(self.solve('a(1). b(X) :- &k{a(X)}. #show a/1. #show b/1.'), [['&k{a(1)}', '&k{b(1)}']])
        self.assert_equal_world_views(self.solve('{a(1)}. b(X) :- &k{a(X)}. #show a/1. #show b/1.'), [['&m{a(1)}']])
        self.assert_equal_world_views(self.solve('{a(1)}. :- not a(1). b(X) :- &k{a(X)}. #show a/1. #show b/1.'), [['&k{a(1)}', '&k{b(1)}']])
        self.assert_equal_world_views(self.solve('''a(1).
            b(X) :- &k{a(X)}.
            c(X) :- &k{b(X)}.
            #show a/1.
            #show b/1.
            #show c/1.'''), [['&k{a(1)}', '&k{b(1)}', '&k{c(1)}']])
        self.assert_equal_world_views(self.solve('''
            {a(1)}. 
            :- not a(1).
            b(X) :- &k{a(X)}.
            c(X) :- &k{b(X)}.
            #show a/1.
            #show b/1.
            #show c/1.'''), [['&k{a(1)}', '&k{b(1)}', '&k{c(1)}']])
        self.assert_equal_world_views(self.solve('-a(1). b(X) :- &k{-a(X)}. #show -a/1. #show b/1.'), [['&k{-a(1)}', '&k{b(1)}']])
        self.assert_equal_world_views(self.solve('{-a(1)}. b(X) :- &k{-a(X)}. #show -a/1. #show b/1.'), [['&m{-a(1)}']])
        self.assert_equal_world_views(self.solve('{-a(1)}. :- not -a(1). b(X) :- &k{-a(X)}. #show -a/1. #show b/1.'), [['&k{-a(1)}', '&k{b(1)}']])
        self.assert_equal_world_views(self.solve('''
            -a(1).
            b(X) :- &k{-a(X)}.
            c(X) :- &k{b(X)}.
            #show -a/1.
            #show b/1.
            #show c/1.'''), [['&k{-a(1)}', '&k{b(1)}', '&k{c(1)}']])
        self.assert_equal_world_views(self.solve('''
            {-a(1)}.
            :- not -a(1).
            b(X) :- &k{-a(X)}.
            c(X) :- &k{b(X)}.
            #show -a/1.
            #show b/1.
            #show c/1.'''), [['&k{-a(1)}', '&k{b(1)}', '&k{c(1)}']])

    def test_show14_non_ground_programs_with_default_negation(self):
        self.assert_equal_world_views(self.solve('''
            a(1).
            b(X) :- &k{ not a(X) }, dom(X).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [['&k{a(1)}', '&k{b(2)}']])
        self.assert_equal_world_views(self.solve('''
            a(1).
            b(X) :- &k{ not not a(X) }, dom(X).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [['&k{a(1)}', '&k{b(1)}']])
        self.assert_equal_world_views(self.solve('''
            b(X) :- &k{ not a(X) }, dom(X).
            c(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [['&k{b(1)}', '&k{b(2)}', '&k{c(1)}', '&k{c(2)}']])
        self.assert_equal_world_views(self.solve('''
            b(X) :- &k{ not not a(X) }, dom(X).
            c(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [[]])
        self.assert_equal_world_views(self.solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- &k{ a(X) }, dom(X).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [['&m{a(1)}', '&m{c(1)}']])
        self.assert_equal_world_views(self.solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- &k{ not a(X) }, dom(X).
            :- b(1).
            :- not b(2).
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            '''), [['&k{b(2)}', '&m{a(1)}', '&m{c(1)}']])
        self.assert_equal_world_views(self.solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            d(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            #show d/1.
            '''), [['&k{b(1)}', '&k{d(1)}', '&m{a(1)}', '&m{c(1)}']])
        self.assert_equal_world_views(self.solve('''
            a(1), c(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            d(X) :- &k{ b(X) }.
            dom(1..2).
            #show a/1.
            #show b/1.
            #show c/1.
            #show d/1.
            '''), [['&k{b(1)}', '&k{d(1)}', '&m{a(1)}', '&m{c(1)}']])

    def test_show15_planning(self):
        self.assert_equal_world_views(self.solve('''
            occurs(pull_trigger,0).
            #show occurs/2.
            '''), [['&k{occurs(pull_trigger,0)}']])