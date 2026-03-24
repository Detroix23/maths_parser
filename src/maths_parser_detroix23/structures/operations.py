"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/operations.py
"""

from maths_parser_detroix23.structures import types, operators


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

	def __repr__(self) -> str:
		return f"Arity0({self.number})"

	def compute(self) -> types.Number:
		return self.number



class Arity2(Operation):
	"""
	# `Arity2`: 2 argument operation.
	"""
	a: Operation
	b: Operation
	operator: operators.Operator

	def __init__(
		self, 
		a: Operation, 
		b: Operation, 
		operator: operators.Operator
	) -> None:
		self.a = a
		self.b = b
		self.operator = operator

	def __str__(self) -> str:
		match self.operator:
			case operators.ADDITION:
				return f"({self.a} + {self.b})"
			case operators.SUBTRACTION:
				return f"({self.a} - {self.b})"
			case operators.MULTIPLICATION:
				return f"({self.a} * {self.b})"
			case operators.DIVISION:
				return f"({self.a} / {self.b})"
			case operators.EXPONENTIATION:
				return f"({self.a} ** {self.b})"
			case _:
				raise SyntaxError(
					f"structures.operations.Arity2.compute() `operator` ({self.operator}) unknown."
				)

	def __repr__(self) -> str:
		return f"Arity2(a={repr(self.a)}, b={repr(self.b)}, operator={self.operator})"

	def compute(self) -> types.Number:
		match self.operator:
			case operators.ADDITION:
				return self.a.compute() + self.b.compute()
			case operators.SUBTRACTION:
				return self.a.compute() - self.b.compute()
			case operators.MULTIPLICATION:
				return self.a.compute() * self.b.compute()
			case operators.DIVISION:
				return self.a.compute() / self.b.compute()
			case operators.EXPONENTIATION:
				return self.a.compute() ** self.b.compute()
			case _:
				raise SyntaxError(
					f"structures.operations.Arity2.compute() `operator` ({self.operator}) unknown."
				)

__all__: list[str] = ["Operation", "Arity0", "Arity2"]
