"""
# Python mathematics parser.
src/maths_parser_detroix23/parsing/builder.py
"""

from maths_parser_detroix23.structures import types, tokens, operators, operations


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
	

def first_operator(token_list: list[tokens.Token | types.Number]) -> int:
	"""
	Choose the first operator, ignoring priorities, from `token_list`.  
	Returns its `int` index. 
	
	Example:
	```
	[1 + 2 * 3 - 3 * 2]
	   ↑
	```
	"""
	i: int = 0
	found: bool = False

	if len(token_list) == 1:
		found = True

	while not found and i < len(token_list):
		token: tokens.Token | types.Number = token_list[i]

		if isinstance(token, operators.Operator):
			found = True

		if not found:
			i += 1

	return i




def first_priority(token_list: list[tokens.Token | types.Number]) -> int:
	"""
	Choose the first operator, respecting priorities, from `token_list`.  
	Returns its `int` index. 
	
	Example:
	```
	[1 + 2 * 3 - 3 * 2]
	       ↑
	```
	"""
	i: int = 0
	found: bool = False
	next_operator: tokens.Token | None
	j: int = 0

	if len(token_list) == 1:
		found = True

	while not found and i < len(token_list):
		token: tokens.Token | types.Number = token_list[i]

		if isinstance(token, operators.Operator):	
			next_operator = None
			j = i + 1
			while next_operator is None and j < len(token_list):
				next_operator_potential: tokens.Token | types.Number = token_list[j] 
				if isinstance(next_operator_potential, operators.Operator):
					next_operator = next_operator_potential

				j += 1
			
			found = (
				next_operator is None
				or token.priority >= next_operator.priority
			)

		if not found:
			i += 1

	return i

def central_operation(token_list: list[tokens.Token | types.Number]) -> int:
	"""
	Find the index of the "center of mass", where to cut, when building the operation three.  
	Thus, to create:
	```python
	Arity2(Brick("..."), Brick("..."), "center of mass operator")
	```
	
	Different methods of determination:
	1. (**Current**) Choose the first operator, respecting priorities.
	2. Choose the first operator, ignoring priorities.
	3. Choose the first irreducible, an operation between plain numbers:

	If `token_list` is of length 1, **returns 0**, to account for single number token list.
	"""
	if len(token_list) == 1:
		return 0
	
	return first_operator(token_list)

