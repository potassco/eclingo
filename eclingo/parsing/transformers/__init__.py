"""
This module is responsible for visiting and rewriting a programs AST to account
for epistemic operators.
"""
from typing import Tuple as _Tuple, List as _List
from clingo import ast as _ast
from .parser_negations import SnReplacementType
from .theory_parser_epistemic import parse_epistemic_literals_elements as _parse_epistemic_literals_elements
from .theory_parser_epistemic import replace_negations_by_auxiliary_atoms_in_epistemic_literals as _replace_negations_by_auxiliary_atoms_in_epistemic_literals
from .theory_parser_epistemic import replace_epistemic_literals_by_auxiliary_atoms as _replace_epistemic_literals_by_auxiliary_atoms
from .theory_parser_epistemic import prefix_to_atom_names as _prefix_to_atom_names

from .parser_negations import strong_negation_auxiliary_rule_replacement

