"""
# Python mathematics parser.
/src/maths_parser_detroix23/__main__.py
"""

from maths_parser_detroix23.structures.operations import *
from maths_parser_detroix23.parsing import tokens

def main() -> None:
	"""
	Main entry point.
	"""
	print("# Python mathematics parser.")

	test_operations1()

	test_tokenize1()

def test_operations1() -> None:
	print("\n## Test: operations 1.")
	E1 = Arity2(
		Arity0(2), 
		Arity2(
			Arity0(2),
			Arity0(3), 
			Operators2.ADDITION
		), 
		Operators2.MULTIPLICATION
		)

	print(E1)
	print(E1.compute())

def test_tokenize1() -> None:
	print("\n## Test: tokenize 1.")
	
	print(tokens.tokenize("11+2*32 / 2 - ( 1 +2)"))
	print(tokens.tokenize("(11+2*32 ) / 2.0 - ( 1,1 +2)*(1)"))
	print(tokens.tokenize("11.232132131"))
	print(tokens.tokenize("((---))"))
	print(tokens.tokenize("12312+123/99    02 "))
	print(tokens.tokenize("1,12 = 123 ? Lol", errors=tokens.TokenizeErrorLevel.IGNORE))
	print(tokens.tokenize("112 = 123 ? Lol", errors=tokens.TokenizeErrorLevel.MARK))
	


main()
