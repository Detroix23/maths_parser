"""
# Python mathematics parser.
/src/maths_parser_detroix23/__main__.py
"""

import pprint
from typing import Sequence

from maths_parser_detroix23.structures import types
from maths_parser_detroix23.structures.tokens import *
from maths_parser_detroix23.structures.operations import *
from maths_parser_detroix23.structures.operators import *

def main() -> None:
	"""
	Main entry point.
	"""
	print("# Python mathematics parser.")

	test_token_struct1()

	test_operations1()

	test_tokenize1()

	test_central_operation1()

def print_list(l: Sequence[object], line: str = " ", end: str = "") -> None:
	print(f"[{line}", end=end)
	for element in l:
		print(f"{element}{line}", end=end)
	print("]", end="\n")

def test_operations1() -> None:
	print("\n## Test: operations 1.")

	print("Operators:", end=" ")
	pprint.pprint(operators)

	E1 = Arity2(
		Arity0(2), 
		Arity2(
			Arity0(2),
			Arity0(3), 
			ADDITION
		), 
		MULTIPLICATION
		)

	print(E1)
	print(E1.compute())

def test_tokenize1() -> None:
	from maths_parser_detroix23.parsing import tokens

	print("\n## Test: tokenize 1.")
	
	print_list(tokens.tokenize("11+2*32 / 2 - ( 1 +2)"))
	print_list(tokens.tokenize("(11+2*32 ) / 2.0 - ( 1.1 +2)*(1)"))
	print_list(tokens.tokenize("11.232132131"))
	print_list(tokens.tokenize("((---))"))
	print_list(tokens.tokenize("12312+123/99    02 "))
	print_list(tokens.tokenize("112 = 123 ? Lol", errors=tokens.TokenizeErrorLevel.IGNORE))
	print_list(tokens.tokenize("112 = 123 ? Lol", errors=tokens.TokenizeErrorLevel.MARK))
	

def test_token_struct1() -> None:
	from maths_parser_detroix23.structures import tokens

	print("Tokens:", end=" ")
	pprint.pprint(tokens.tokens)

def test_central_operation1() -> None:
	from maths_parser_detroix23.parsing import tokens, builder

	print("\n## Test: Central operation 1.")

	expressions: list[str] = []
	expressions.append("11+2*32 / 2 - ( 1 +2)")
	expressions.append("(11+2*32 ) ^ 2.0 - ( 1.1 +2)*(1)")
	expressions.append("11.232132131")
	expressions.append("((---))")
	expressions.append("12312+123/99    02 ")


	for expression in expressions:
		print(expression)
		token_list: list[Token | types.Number] = tokens.tokenize(expression)
		print("- ", end="")
		print_list(token_list)
		centre: int = builder.central_operation(token_list)
		print(f"- {centre}, {token_list[centre]}")

main()
