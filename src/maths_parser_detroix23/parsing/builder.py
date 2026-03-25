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


def parse(block: tokens.Block) -> operations.Operation:
	"""
	Recursively parse `token_list` into an `Operation`.

	*Base cases*:
	- Singleton of a `Number` `n` => `Arity0(n)`.

	*Errors*:
	- Singleton of an `Operator`;
	- Empty list;
	- Split is not an `Operator`.
	"""
	if len(block) == 0:
		raise ValueError(f"parsing.builder.parse() `token_list` empty.")
	
	if len(block) == 1:
		single: tokens.Token | types.Number = block[0]

		if types.in_union(single, types.Number):
			return operations.Arity0(single)  # pyright: ignore[reportArgumentType]
		elif isinstance(single, tokens.Block):
			return parse(single)
		else:
			raise ArithmeticError(f"parsing.builder.parse() One element `token_list` not a number ({repr(single)}).")
	
	split_index: int = split.choose(block.expression)
	if split_index >= len(block):
		raise IndexError(f"parsing.builder.parse() `token_list` = {block}, `split_index` = {split_index}.")

	split_operator: tokens.Token | types.Number = block[split_index]

	if not isinstance(split_operator, operators.Operator):
		raise ArithmeticError(f"parsing.builder.parse() Split on position i={split_index} is not an `Operator` ({split_operator}).")

	block_left = tokens.Block(block.expression[:split_index], block.depth)
	block_right = tokens.Block(block.expression[split_index + 1:], block.depth)

	return operations.Arity2(
		parse(block_left),
		parse(block_right),
		split_operator,
	)
