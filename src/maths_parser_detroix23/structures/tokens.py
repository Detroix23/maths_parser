"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/tokens.py
"""

from typing import Final

from maths_parser_detroix23.structures import defaults, types

tokens: list[Token] = []
""" Register all `Token`s: one centralized access. """

class Token:
	"""
	# `Token` trait for all symbols.
	Holds:
	- `representations`: `list[str]`
	"""
	representations: list[str]

	def __init__(self, representations: list[str]) -> None:
		"""
		Initialize a basic `Token` with its `representations` (at least one).

		Also register it`self` into `tokens`.
		"""
		self.representations = representations

		tokens.append(self)
	
	def __str__(self) -> str:
		"""
		Returns the first `representations` of the `Token` 
		"""
		return self.representations[0]

	def __repr__(self) -> str:
		"""
		Returns a string: `Token(representations)`.
		"""
		return f"Token(representations={self.representations})"


class Block(Token):
	"""
	Parenthesis priority block.
	- String expression
	- Without the parenthesis characters
	"""
	expression: types.Tokens
	depth: int

	def __init__(self, expression: types.Tokens, depth: int) -> None:
		self.expression = expression
		self.depth = depth

	def __str__(self) -> str:
		return f"({' '.join([str(value) for value in self.expression])})"

	def __repr__(self) -> str:
		return f"Block({self.expression}, depth={self.depth})"

	def __len__(self) -> int:
		return len(self.expression)
	
	def __getitem__(self, index: int) -> Token | types.Number:
		return self.expression[index] 

UNKNOWN: Final[Token] = Token([defaults.UNKNOWN_TOKEN])
BLOCK_OPENING: Final[Token] = Token(["("])
BLOCK_CLOSING: Final[Token] = Token([")"])
	