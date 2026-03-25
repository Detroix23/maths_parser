"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/types.py
"""

from types import UnionType
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
	from maths_parser_detroix23.structures import tokens
	
def in_union(value: object, union: UnionType) -> bool:
	"""
	Check if type `t` is in `union`.
	"""
	for type_union in union.__args__:
		if type(value) is type_union:
			return True
	
	return False

Number = Union[int, float]
"""**type** `Number` used in the whole script."""

Tokens = list[Union['tokens.Token', Number]]
"""**type** `Tokens` list. """
