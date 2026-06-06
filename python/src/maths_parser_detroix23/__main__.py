"""
# Python mathematics parser.
/src/maths_parser_detroix23/__main__.py
"""

from maths_parser_detroix23.tests import (
	test_token_struct1,
	test_operations1,
	test_tokenize1,
	test_central_operation1,
	test_parenthesis_package1,
	test_parse1,
)

def main() -> None:
	"""
	Main entry point.
	"""
	print("# Python mathematics parser.")

	test_token_struct1()

	test_operations1()

	test_tokenize1()

	test_central_operation1()

	test_parenthesis_package1()

	test_parse1()

main()
