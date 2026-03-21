"""
# Python mathematics parser.
src/maths_parser_detroix23/parsing/builder.py
"""

from maths_parser_detroix23.structures import defaults, operators, operations


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

	def compute(self) -> int | float:
		raise NotImplementedError(f"parsing.builder.Brick.compute() `Brick` can't be computed.")
	

def central_operation(tokens: list[str]) -> int:
	"""
	Find the index of the "center of mass", where to cut, when building the operation three.  
	Thus, to create:
	```python
	Arity2(Brick("..."), Brick("..."), "center of mass operator")
	```
	
	Different methods of determination:
	1. (**Current**) Choose the first operator, respecting priorities.
	```
	[1 + 2 * 3 - 3 * 2]
	       ↑
	```
	2. Choose the irreducible, an operation between plain numbers:
	```
	[(1 + (2 * (3 - 1)) / (2 - 1)]
	              ↑
	```
	"""
	i: int = 0
	found: bool = False
	next_operator: str | None
	j: int = 0

	while not found and i < len(tokens):
		if tokens[i] in defaults.OPERATORS:
			next_operator = None
			j = i + 1
			while next_operator is None and j < len(tokens):
				if tokens[i] in defaults.OPERATORS:
					next_operator = tokens[i] 

			found = (
				next_operator is None
				or operators.PRIORITIES[tokens[i]] >= operators.PRIORITIES[next_operator]
			)

		i += 1
