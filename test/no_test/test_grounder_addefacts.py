import unittest
import eclingo
from literals import *
from eclingo.util.logger import silent_logger
from eclingo.grounder import EpistemicSignature


class TestGrounderAddEfacts(unittest.TestCase):

    def setUp(self):
        self.control  = eclingo.util.clingoext.Control(logger=silent_logger)
        self.control.configuration.solve.models  = 0
        self.grounder = eclingo.grounder.Grounder(self.control)


class TestGrounderAddEfactsPositive(TestGrounderAddEfacts):

    def test_fact(self):
        program = "a."
        facts     = sorted([a])
        non_facts = sorted([])
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)

    def test_fact_sn(self):
        program = "-a."
        facts     = sorted([sna])
        non_facts = sorted([])
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)


    def test_cycle(self):
        program = """
        a :- not b.
        b :- not a.
        """
        facts     = sorted([])
        non_facts = sorted([a, b])
        models    = [[a], [b]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)

    def test_fact_k(self):
        program = """
        a.
        b :- &k{ a }.
        """
        facts     = sorted([a])
        non_facts = sorted([b, ka])
        efacts    = sorted([ka])
        signature = dict()
        models    = [[ka, b]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_missing_fact_k(self):
        program = """
        -a.
        b :- &k{ a }.
        """
        facts     = sorted([sna])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_cycle_k(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ a }.
        """
        facts     = sorted([])
        non_facts = sorted([a, b, c, ka])
        efacts    = sorted([])
        models    = [[ka, a, b], [a], [c]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        a_code    = self.grounder.symbol_to_atom[a]
        ka_code   = self.grounder.symbol_to_atom[ka]
        signature = {ka_code: EpistemicSignature(
            epistemic_literal=ka,
            code=ka_code,
            literal=None,
            test_atom=a,
            test_atom_code=a_code)}
        # self.assertEqual(self.grounder.epistemic_signature, signature)
        

class TestGrounderAddEfactsDefaultNegation(TestGrounderAddEfacts):


    def test_fact_knot(self):
        program = """
        a.
        b :- &k{ not a }.
        """
        facts     = sorted([a])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_fact_knotnot(self):
        program = """
        a.
        b :- &k{ not not a }.
        """
        facts     = sorted([a, not2a])
        non_facts = sorted([b, knot2a])
        efacts    = sorted([knot2a])
        signature = dict()
        models    = [[knot2a, b]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)



    def test_missing_fact_knot(self):
        program = """
        -a.
        b :- &k{ not a }.
        """
        facts     = sorted([sna, nota])
        non_facts = sorted([b, knota])
        efacts    = sorted([knota])
        signature = dict()
        models    = [[b, knota]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)

    def test_missing_fact_knotnot(self):
        program = """
        -a.
        b :- &k{ not not a }.
        """
        facts     = sorted([sna])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)

    def test_cycle_knot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not a }.
        """
        facts     = sorted([])
        non_facts = sorted([knota, nota, a, b, c])
        efacts    = sorted([])
        signature = dict()
        models    = [[knota, nota, b, c], [a], [c, nota]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        nota_code    = self.grounder.symbol_to_atom[nota]
        knota_code   = self.grounder.symbol_to_atom[knota]
        signature = {knota_code: EpistemicSignature(
            epistemic_literal=knota,
            code=knota_code,
            literal=None,
            test_atom=nota,
            test_atom_code=nota_code)}
        # self.assertEqual(self.grounder.epistemic_signature, signature)

    def test_cycle_knotnot(self):
        program = """
        a :- not c.
        c :- not a.
        b :- &k{ not not a }.
        """
        facts     = sorted([])
        non_facts = sorted([a, not2a, c, b, knot2a])
        efacts    = sorted([])
        signature = dict()
        models    = [[knot2a, b, a, not2a], [a, not2a], [c]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        not2a_code    = self.grounder.symbol_to_atom[not2a]
        knot2a_code   = self.grounder.symbol_to_atom[knot2a]
        signature = {knot2a_code: EpistemicSignature(
            epistemic_literal=knot2a,
            code=knot2a_code,
            literal=None,
            test_atom=not2a,
            test_atom_code=not2a_code)}
        # self.assertEqual(self.grounder.epistemic_signature, signature)

class TestGrounderAddEfactsStrongNegation(TestGrounderAddEfacts):
    
    def test_fact_ksn(self):
        program = """
        -a.
        b :- &k{ -a }.
        """
        facts     = sorted([sna, ec_sna])
        non_facts = sorted([b, ksna])
        efacts    = sorted([ksna])
        signature = dict()
        models    = [[ksna, b]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_fact_knotsn(self):
        program = """
        -a.
        b :- &k{ not -a }.
        """
        facts     = sorted([sna])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_fact_knotnotsn(self):
        program = """
        -a.
        b :- &k{ not not -a }.
        """
        facts     = sorted([sna, not2sna])
        non_facts = sorted([b, knot2sna])
        efacts    = sorted([knot2sna])
        signature = dict()
        models    = [[knot2sna, b]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)

    
    def test_missing_fact_ksn(self):
        program = """
        a.
        b :- &k{ -a }.
        """
        facts     = sorted([a])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_missing_fact_knotsn(self):
        program = """
        a.
        b :- &k{ not -a }.
        """
        facts     = sorted([a, notsna])
        non_facts = sorted([b, knotsna])
        efacts    = sorted([knotsna])
        signature = dict()
        models    = [[b, knotsna]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)


    def test_missing_fact_knotnotsn(self):
        program = """
        a.
        b :- &k{ not not -a }.
        """
        facts     = sorted([a])
        non_facts = sorted([])
        efacts    = sorted([])
        signature = dict()
        models    = [[]]
        for model in models:
            model.extend(facts)
        models    = sorted(sorted(model) for model in models)
        self.grounder.add_program(program)
        self.grounder.ground()
        self.assertEqual(sorted(self.grounder.facts), facts)
        self.assertEqual(sorted(self.grounder.symbol_to_atom.keys()), non_facts)

        obtained_models = []
        with self.control.solve(yield_=True) as handle:
            for model in handle:
                obtained_models.append(sorted(model.symbols(shown=True)))
        for model in obtained_models:
            model.sort()
        obtained_models.sort()
        self.assertEqual(obtained_models, models)
        self.assertEqual(sorted(e.epistemic_literal for e in self.grounder.epistemic_facts), efacts)
        # self.assertEqual(self.grounder.epistemic_signature, signature)
        