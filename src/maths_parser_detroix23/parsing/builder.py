"""
# Python mathematics parser.
src/maths_parser_detroix23/parsing/builder.py
"""

from maths_parser_detroix23.structures import types, tokens, operators, operations
from maths_parser_detroix23.parsing import split


class Brick(operations.Operation):
	"""
	# `Brick` of a partially parsed operation.
	Contains a `str` of the yet to be parsed expression.
	"""
	expression: str

	def __init__(self, expression: str) -> None:
		self.expression = expression

	def __str__(self) -> str:
		"""
		Returns `Brick(self.expression)`. 
		"""	
		return f"Brick({self.expression})"

	def compute(self) -> types.Number:
		raise NotImplementedError(f"parsing.builder.Brick.compute() `Brick` can't be computed.")


def parse(token_list: list[tokens.Token | types.Number]) -> operations.Operation:
	"""
	Recursively parse `token_list` into an `Operation`.

	*Base cases*:
	- Singleton of a `Number` `n` => `Arity0(n)`.

	*Errors*:
	- Singleton of an `Operator`;
	- Empty list;
	- Split is not an `Operator`.
	"""
	if len(token_list) == 0:
		raise ValueError(f"parsing.builder.parse() `token_list` empty.")
	
	if len(token_list) == 1:
		single: tokens.Token | types.Number = token_list[0]

		if types.in_union(single, types.Number):
			return operations.Arity0(single)  # pyright: ignore[reportArgumentType]
		else:
			raise ArithmeticError(f"parsing.builder.parse() One element `token_list` not a number ({repr(single)}).")
	
	split_index: int = split.choose(token_list)
	if split_index >= len(token_list):
		raise IndexError(f"parsing.builder.parse() `token_list` = {token_list}, `split_index` = {split_index}.")

	split_operator: tokens.Token | types.Number = token_list[split_index]

	if not isinstance(split_operator, operators.Operator):
		raise ArithmeticError(f"parsing.builder.parse() Split on position i={split_index} is not an `Operator` ({split_operator}).")

	return operations.Arity2(
		parse(token_list[:split_index]),
		parse(token_list[split_index + 1:]),
		split_operator,
	)
