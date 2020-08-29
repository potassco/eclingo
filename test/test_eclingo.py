import unittest
import eclingo as _eclingo


def solve(program):
    control  = _eclingo.internal_states.InternalStateControl(message_limit=0)
    control.configuration.solve.models  = 0
    config   = _eclingo.config.AppConfig()
    config.eclingo_semantics = "c19-1"
    econtrol = _eclingo.control.Control(control=control, config=config)
    # econtrol.config.eclingo_verbose = 10

    econtrol.add_program(program)
    world_views = []
    for world_view in econtrol.solve():
        world_view = sorted(str(symbol) for symbol in world_view.symbols)
        world_views.append(world_view)
    return sorted(world_views)


class TestCase(unittest.TestCase):

    def assert_models(self, models, expected):
        self.assertEqual(models, sorted(sorted(wv) for wv in expected))


class TestEclingoGround(TestCase):

    def test_objective_programs(self):
        self.assert_models(solve('a.'), [[]])

    def test_positive_programs(self):
        self.assert_models(solve('a. b :- &k{a}.'), [['&k{a}']])
        self.assert_models(solve('{a}. b :- &k{a}.'), [[]])
        self.assert_models(solve('{a}. :- not a. b :- &k{a}.'), [['&k{a}']])
        self.assert_models(solve('a. b :- &k{a}. c :- &k{b}.'), [['&k{a}', '&k{b}']])
        self.assert_models(solve('{a}. :- not a. b :- &k{a}. c :- &k{b}.'), [['&k{a}', '&k{b}']])

    def test_programs_with_strong_negation(self):
        self.assert_models(solve('-a. b :- &k{-a}.'), [['&k{-a}']])
        self.assert_models(solve('{-a}. b :- &k{-a}.'), [[]])
        self.assert_models(solve('{-a}. :- not -a. b :- &k{-a}.'), [['&k{-a}']])
        self.assert_models(solve('-a. b :- &k{-a}. c :- &k{b}.'), [['&k{-a}', '&k{b}']])
        self.assert_models(solve('{-a}. :- not -a. b :- &k{-a}. c :- &k{b}.'), [['&k{-a}', '&k{b}']])

    def test_programs_with_default_negation(self):
        self.assert_models(solve('a. b :- &k{ not a }.'), [[]])
        self.assert_models(solve('a. b :- &k{ not not a }.'), [['&k{not not a}']])
        self.assert_models(solve('b :- &k{ not a }. c :- &k{ b }.'), [['&k{b}']]) # this failed in eclingo
        self.assert_models(solve('b :- &k{ not not a }. c :- &k{ b }.'), [[]])
        self.assert_models(solve('''
            a :- not c.
            c :- not a.
            b :- &k{ a }.
            :- b.
            '''), [[]])
        self.assert_models(solve('''
            a :- not c.
            c :- not a.
            b :- &k{ not a }.
            :- b.
            '''), [['&m{a}']])
        self.assert_models(solve('''
            a :- not c.
            c :- not a.
            b :- not &k{ not a }.
            d :- &k{ b }.
            '''), [['&k{b}', '&m{a}']])
        self.assert_models(solve('''
            a, c.
            b :- not &k{ not a }.
            d :- &k{ b }.
            '''), [['&k{b}', '&m{a}']])


class TestEclingoNonGround(TestCase):

    def test_objective_programs(self):
        self.assert_models(solve('a(1).'), [[]])

    def test_positive_programs(self):
        self.assert_models(solve('a(1). b :- &k{a(X)}.'), [['&k{a(1)}']])
        self.assert_models(solve('{a(1)}. b :- &k{a(X)}.'), [[]])
        self.assert_models(solve('{a(1)}. :- not a(1). b :- &k{a(X)}.'), [['&k{a(1)}']])
        self.assert_models(solve('a(1). b :- &k{a(X)}. c :- &k{b}.'), [['&k{a(1)}', '&k{b}']])
        self.assert_models(solve('{a(1)}. :- not a(1). b :- &k{a(X)}. c :- &k{b}.'), [['&k{a(1)}', '&k{b}']])

    def test_programs_with_strong_negation(self):
        self.assert_models(solve('-a(1). b :- &k{-a(X)}.'), [['&k{-a(1)}']])
        self.assert_models(solve('{-a(1)}. b :- &k{-a(X)}.'), [[]])
        self.assert_models(solve('{-a(1)}. :- not -a(1). b :- &k{-a(X)}.'), [['&k{-a(1)}']])
        self.assert_models(solve('-a(1). b :- &k{-a(X)}. c :- &k{b}.'), [['&k{-a(1)}', '&k{b}']])
        self.assert_models(solve('{-a(1)}. :- not -a(1). b :- &k{-a(X)}. c :- &k{b}.'), [['&k{-a(1)}', '&k{b}']])

    def test_programs_with_default_negation(self):
        self.assert_models(solve('a(1). b :- &k{ not a(X) }, dom(X). dom(1..2).'), [[]])
        self.assert_models(solve('a(1). b :- &k{ not not a(X) }, dom(X). dom(1..2).'), [['&k{not not a(1)}']])
        self.assert_models(solve('b :- &k{ not a(X) }, dom(X). dom(1..2). c :- &k{ b }.'), [['&k{b}']])
        self.assert_models(solve('b :- &k{ not not a(X) }, dom(X). dom(1..2). c :- &k{ b }.'), [[]])
        self.assert_models(solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- &k{ a(X) }, dom(X).
            :- b(X), dom(X).
            dom(1..2).
            '''), [[]])
        self.assert_models(solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- &k{ not a(X) }, dom(X).
            dom(1..2).
            :- b(1).
            :- not b(2).
            '''), [['&m{a(1)}']])
        self.assert_models(solve('''
            a(1) :- not c(1).
            c(1) :- not a(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            dom(1..2).
            d(X) :- &k{ b(X) }.
            '''), [['&m{a(1)}', '&k{b(1)}']])
        self.assert_models(solve('''
            a(1), c(1).
            b(X) :- not &k{ not a(X) }, dom(X).
            dom(1..2).
            d(X) :- &k{ b(X) }.
            '''), [['&m{a(1)}', '&k{b(1)}']])


    def test_grounding_simplifications(self):
        self.assert_models(solve('''
            dom(1..2).
            :- &k{ a(X) }, not a(X), dom(X).
            a(1).
            {a(2)}.
            :- {a(2)} = 0.
            '''), [['&k{a(1)}', '&k{a(2)}']])


class TestEclingoAggregates(TestCase):

    def test_ground_programs(self):
        self.assert_models(solve('''
            a.
            b :- a.
            c :- &k{b}.
            d :- &k{c}.
            '''), [['&k{b}', '&k{c}']])

        self.assert_models(solve('''
            a.
            b :- #count{a} >= 1.
            c :- &k{b}.
            d :- &k{c}.
            '''), [['&k{b}', '&k{c}']])

        self.assert_models(solve('''
            a :- not &k{ not a}.
            b :- a.
            c :- &k{b}.
            d :- &k{c}.
            '''), [[], ['&m{a}', '&k{b}', '&k{c}']])

        self.assert_models(solve('''
            {fact}.
            :- not fact.
            a :- not &k{ not a}.
            b :- #sum{1:fact; 25:a} >= 24.
            c :- &k{b}.
            d :- &k{c}.
            '''), [[], ['&m{a}', '&k{b}', '&k{c}']])



class TestEclingoCommontToAllSemantics(TestCase):

    def test_ground_programs(self):
        self.assert_models(solve('a, b.'), [[]])
        self.assert_models(solve('a, b. a :- &k{b}.'), [[]])
        self.assert_models(solve('a, b. a :- not &k{b}.'), [[]])
        self.assert_models(solve('a, b. c :- not &k{b}.'), [[]])
        self.assert_models(solve('a :- not &k{b}. b :- not &k{a}.'), [['&k{a}'], ['&k{b}']])
        self.assert_models(solve('a. a :- not &k{a}. :- &k{not a}.'), [['&k{a}']])


class TestEclingoCommontTo_G94_G11_FAEEL(TestCase): # pylint: disable=invalid-name

    def test_ground_programs(self):
        self.assert_models(solve('a :- not &k{not a}.'), [[], ['&m{a}']])
        self.assert_models(solve('a, b. a :- not &k{ not b}.'), [])
        self.assert_models(solve('a, b. a :- &k{ not b}.'), [[], ['&m{b}']])
        self.assert_models(solve('a :- b. b :- not &k{ not a}.'), [[], ['&m{a}']])
        self.assert_models(solve('a :- not &k{ not b}. b :- not &k{ not a}.'), [[], ['&m{a}', '&m{b}']])
        self.assert_models(solve('a :- not &k{not b}, not b. b :- not &k{not a}, not a.'), [[], ['&m{a}', '&m{b}']])

class TestEclingoCommontTo_G11_FAEEL(TestCase): # pylint: disable=invalid-name

    def test_ground_programs(self):
        self.assert_models(solve('a :- &k{a}.'), [[]])
        self.assert_models(solve('a :- &k{a}. a:- not &k{a}.'), [])


class TestEclingoUnfounded(TestCase): # pylint: disable=invalid-name

    def test_ground_programs(self):
        self.assert_models(solve('''
            a, b.
            a :- &k{b}. 
            b :- &k{a}.
        '''), [[], ['&k{a}', '&k{b}']])
        self.assert_models(solve('''
            {a}.
            b :- a. 
            c :- not a.
            c :- &k{b}. 
            b :- &k{c}.
        '''), [[], ['&k{b}', '&k{c}']])
