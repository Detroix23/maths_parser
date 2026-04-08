"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/operators.py
"""

from typing import Final

from maths_parser_detroix23.structures import tokens

operators: list[Operator] = []
""" Register all `Operator`s: centralized list. """

class Operator(tokens.Token):
	"""
	# `Operator` trait for all operators.
	"""
	arity: int
	priority: int

	def __init__(
		self,
		arity: int,
		priority: int,
		representations: list[str],
	) -> None:
		"""
		Initialize an `Operator` with `arity`, a `priority` and some string `representations`.

		It also initialize the underlying `Token`, and register it`self` in `operators`.
		"""
		super().__init__(representations)
		self.arity = arity
		self.priority = priority

		operators.append(self)

	def __repr__(self) -> str:
		return f"Operator(arity={self.arity}, priority={self.priority}, representations={self.representations})"
	

ADDITION: Final[Operator] = Operator(2, 1, ["+"])
SUBTRACTION: Final[Operator] = Operator(2, 1, ["-"])
MULTIPLICATION: Final[Operator] = Operator(2, 2, ["*"])
DIVISION: Final[Operator] = Operator(2, 2, ["/"])
EXPONENTIATION: Final[Operator] = Operator(2, 3, ["^", "**"])


__all__: list[str] = [
	"operators",
	"Operator", 
	"ADDITION", 
	"SUBTRACTION", 
	"MULTIPLICATION", 
	"DIVISION", 
	"EXPONENTIATION", 
]
