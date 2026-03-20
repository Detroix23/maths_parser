"""
# Python mathematics parser.
/src/maths_parser_detroix23/__main__.py
"""

from maths_parser_detroix23.structures.operations import *

def main() -> None:
	"""
	Main entry point.
	"""
	print("# Python mathematics parser.")

	test_operations1()


def test_operations1() -> None:
	
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

main()
