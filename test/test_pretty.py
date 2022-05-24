import unittest

import clingo
from clingo import Function, Number

import eclingo.util.clingoext as clingoext
from eclingo.util.logger import silent_logger

from eclingo.util.groundprogram import ClingoOutputAtom, ClingoProject, ClingoRule, GroundProgram, PrettyGroundProgram


class Test(unittest.TestCase):


    def test_clingo_symbol_function(self):
        symbol=Function("b", [Number(1)], True)
        # p=PrettyGroundProgram(symbol)

        self.assertEqual(str(symbol), 'b(1)')


    def test_clingo_output_atom_pretty(self):
        
        s = [ClingoOutputAtom(symbol=Function("b", [Number(1)], True), atom=0, order=0)]
        p = PrettyGroundProgram(s)

        self.assertEqual(str(p),'b(1).')


    def test_doubleNegation(self):

        program = """
        {d}.
        e :- not not d.
        """

        expected = """ 
        {d}.
        e :- not x_2.
        x_2 :- not d.
        """

        self.control = clingoext.Control(logger=silent_logger)


        self.control.configuration.solve.project = "auto,3"
        self.control.configuration.solve.models  = 0

        self.control.add("base", [], program)
        self.control.ground([("base", [])])

        self.assertEqual(str(self.control.ground_program).replace(' ','').replace('\n',''), expected.replace(' ','').replace('\n',''))



