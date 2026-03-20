"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/operations.py
"""

import enum

from maths_parser_detroix23.structures import types

class Operators2(enum.Enum):
	"""
	# `Operators2` of 2-arity.
	"""
	ADDITION = 0
	SUBTRACTION = 1
	MULTIPLICATION = 2
	DIVISION = 3
	EXPONENTIATION = 4

class Operation:
	"""
	# `Operation` trait.
	Define the backbone, most basic behaviors.
	"""
	def __init__(self) -> None:
		"""
		Initialize an operation.  
		As is, it must be overloaded or it will raise a `NotImplementedError`.
		"""	
		raise NotImplementedError(
			"structures.operations.Operation.__init__() `Operation` must be overloaded."
		)
	
	def __str__(self) -> str:
		"""
		Return a human and nicely readable representation of the `Operation`.  
		As is, it must be overloaded or it will raise a `NotImplementedError`.
		"""
		raise NotImplementedError(
			"structures.operations.Operation.compute() `Operation` must be overloaded."
		)

	def compute(self) -> types.Number:
		"""
		Compute and return the result of the operation recursively.  
		As is, it must be overloaded or it will raise a `NotImplementedError`.
		"""
		raise NotImplementedError(
			"structures.operations.Operation.compute() `Operation` must be overloaded."
		)

class Arity0(Operation):
	"""
	# `Arity0`: Number.
	"""
	number: types.Number

	def __init__(self, number: types.Number) -> None:
		self.number = number

	def __str__(self) -> str:
		return f"{self.number}"

	def compute(self) -> types.Number:
		return self.number



class Arity2(Operation):
	"""
	# `Arity2`: 2 argument operation.
	"""
	a: Operation
	b: Operation
	operator: Operators2

	def __init__(
		self, 
		a: Operation, 
		b: Operation, 
		operator: Operators2
	) -> None:
		self.a = a
		self.b = b
		self.operator = operator

	def __str__(self) -> str:
		match self.operator:
			case Operators2.ADDITION:
				return f"({self.a} + {self.b})"
			case Operators2.SUBTRACTION:
				return f"{self.a} - {self.b}"
			case Operators2.MULTIPLICATION:
				return f"{self.a} * {self.b}"
			case Operators2.DIVISION:
				return f"{self.a} / {self.b}"
			case Operators2.EXPONENTIATION:
				return f"{self.a} ** {self.b}"
			case _:
				raise SyntaxError(
					f"structures.operations.Arity2.compute() `operator` ({self.operator}) unknown."
				)

	def compute(self) -> types.Number:
		match self.operator:
			case Operators2.ADDITION:
				return self.a.compute() + self.b.compute()
			case Operators2.SUBTRACTION:
				return self.a.compute() - self.b.compute()
			case Operators2.MULTIPLICATION:
				return self.a.compute() * self.b.compute()
			case Operators2.DIVISION:
				return self.a.compute() / self.b.compute()
			case Operators2.EXPONENTIATION:
				return self.a.compute() ** self.b.compute()
			case _:
				raise SyntaxError(
					f"structures.operations.Arity2.compute() `operator` ({self.operator}) unknown."
				)

__all__: list[str] = ["Operators2", "Operation", "Arity0", "Arity2"]
