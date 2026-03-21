"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/tokens.py
"""

from typing import Final

from maths_parser_detroix23.structures import defaults

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


UNKNOWN: Final[Token] = Token([defaults.UNKNOWN_TOKEN])
BLOCK_OPENING: Final[Token] = Token(["("])
BLOCK_CLOSING: Final[Token] = Token([")"])
	