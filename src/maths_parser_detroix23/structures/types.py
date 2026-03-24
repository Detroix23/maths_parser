"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/types.py
"""

from types import UnionType

def in_union(value: object, union: UnionType) -> bool:
	"""
	Check if type `t` is in `union`.
	"""
	for type_union in union.__args__:
		if type(value) is type_union:
			return True
	
	return False

Number = int | float
"""**type** `Number` used in the whole script."""
