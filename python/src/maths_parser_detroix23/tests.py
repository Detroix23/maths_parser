"""
# Python mathematics parser.
/src/maths_parser_detroix23/tests.py
"""

import pprint
from typing import Sequence

from maths_parser_detroix23.structures import types
from maths_parser_detroix23.structures.tokens import Token
from maths_parser_detroix23.structures.operations import (
    Operation, 
    Arity0, 
    Arity2
)
from maths_parser_detroix23.structures.operators import (
    operators,
    ADDITION,
    MULTIPLICATION,
)
from maths_parser_detroix23.structures.tokens import Block

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
	from maths_parser_detroix23.parsing import tokens, split

	print("\n## Test: Central operation 1.")

	expressions: list[str] = [
		"11+2*32 / 2 - ( 1 +2)",
		"(11+2*32 ) ^ 2.0 - ( 1.1 +2)*(1)",
		"11.232132131",
		"((---))",
		"12312+123/99    02 ",
	]

	for expression in expressions:
		print(expression)
		token_list: list[Token | types.Number] = tokens.tokenize(expression)
		print("- Tokenized: ", end="")
		print_list(token_list)
		center: int = split.choose(token_list)
		print(f"- Center: i={center}, {token_list[center]} {type(token_list[center])}")

def test_parenthesis_package1() -> None:
	from maths_parser_detroix23.parsing import tokens, parenthesis

	print("\n## Parenthesis packaging.")

	expressions: list[str] = [
		"1 + 2 * 3", 
		"( 5 + 2 * 3 - 88 )", 
		"1 + ( 1 )", 
		"5-3*( 9 - ( ( 1 + 6 ) / 2 ) )", 
		"1 + ( 2 * 3 )", 
		"()", 
	]

	for expression in expressions:
		packaged: Block = parenthesis.package(tokens.tokenize(expression))
		print(expression)
		print(f"- {packaged}")
		print(f"- {repr(packaged)}")

def test_parse1() -> None:
    from maths_parser_detroix23.parsing import tokens, parenthesis, builder

    print("\n## Test: Parse 1.")

    expressions: list[tuple[str, float]] = [
        ("11+2*32 / 2 - 1 + 2 ", 44.0),
        ("(11+2*32 ) ^ 2.0 - ( 1.1 +2)*(1)", 5621.9),
        ("(2 - 1) * (4 - 12 / 3)", 0.0),
        ("11.232132131", 11.232132131),
        ("12312+123/9902 ", 12312.012421732983),
    ]

    for expression, excepted in expressions:
        print(expression)
        
        token_list: list[Token | types.Number] = tokens.tokenize(expression)
        print("- Tokenized: ", end="")
        print_list(token_list)
        
        block: Block = parenthesis.package(token_list)
        print(f"- Packaged: {block}")

        parsed: Operation = builder.parse(block)
        print(f"- Parsed: {parsed}")
        computed: int | float = parsed.compute()
        print(f" Recomputed: {computed}")

        assert excepted == computed

    print("☑ Passed asserts: Parse 1.")

    return
