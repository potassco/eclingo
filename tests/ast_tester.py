from pprint import pformat
from typing import Any, MutableMapping, MutableSequence, Sequence
from unittest import TestCase

from clingo.ast import AST
from clingox.ast import ast_to_dict


def remove_key_recursively(value: Any, key: Any) -> None:
    """
    This function removes the given key from any mutable mappings contained in
    in the given value composed of nested sequences, mutable mappings, and
    other values.
    """
    if isinstance(value, MutableMapping):
        if key in value:
            del value[key]
        for element in value.values():
            remove_key_recursively(element, key)
    elif isinstance(value, Sequence) and not isinstance(value, str):
        for element in value:
            remove_key_recursively(element, key)


class ASTTestCase(TestCase):
    def assertASTEqual(self, first, second, msg=None):
        first_dict = ast_to_dict(first)
        second_dict = ast_to_dict(second)
        remove_key_recursively(first_dict, "location")
        remove_key_recursively(second_dict, "location")
        ast_msg = f"""\n
{str(first)} != {str(second)}

{str(pformat(first_dict, sort_dicts=True,))}
{str(pformat(second_dict, sort_dicts=True,))}
        """
        super().assertEqual(first_dict, second_dict, ast_msg)
        super().assertEqual(first, second, ast_msg)

    def assertEqual(self, first, second, msg=None):
        if isinstance(first, AST) and isinstance(second, AST):
            return self.assertASTEqual(first, second, msg)
        return super().assertEqual(first, second, msg)
