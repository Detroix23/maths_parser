"""
# Python mathematics parser.
src/maths_parser_detroix23/parsing/tokens.py
"""

import enum

from maths_parser_detroix23.structures import defaults

class TokenizeErrorLevel(enum.Enum):
	STRICT = 0
	"""Raise an exception."""
	MARK = 1
	"""Puts a `UNKNOWN_TOKEN` marker."""
	IGNORE = 2
	"""Ignore the invalid character."""

def is_numeric(expression: str) -> bool:
	"""
	Return if the `expression` can compose or is a number:
	- digit,
	- dot (`.`),
	- comma (`,`),
	- underscore (`_`).
	"""
	for character in expression:
		if not character.isdigit() and not character in defaults.NUMBER_SYMBOLS:
			return False
	
	return expression != ""

def is_structural(expression: str) -> bool:
	"""
	Return if the `expression` is an operator or a set of parenthesis.
	"""
	return (
		expression in defaults.PARENTHESIS
		or expression in defaults.OPERATORS
	)

def tokenize(
	expression: str, 
	errors: TokenizeErrorLevel = TokenizeErrorLevel.STRICT,
) -> list[str]:
	"""
	Divide the string `expression` into a `list` of `str` tokens:
	- a number (one token comprises all the digits, and the dot),
	- an operator,
	- a parenthesis. 
	"""
	tokens: list[str] = []
	cursor: int = 0
	token: str = ""
	building: bool = False
	character: str

	while cursor < len(expression):
		character = expression[cursor]
		# print(f"i={cursor}, {character}")

		if is_numeric(character):
			if not building:
				token = ""

			building = True
			token += character
			
		elif character in defaults.SPACE:
			building = True

		elif is_structural(character):
			if is_numeric(token):
				tokens.append(token)
			
			building = False
			token = character

		else:
			if errors == TokenizeErrorLevel.STRICT:
				raise SyntaxError(f"parsing.tokens.tokenize() `STRICT` token unknown: `{character}`.")

			elif errors == TokenizeErrorLevel.MARK:
				if is_numeric(token):
					tokens.append(token)
				building = False
				token = defaults.UNKNOWN_TOKEN

		if not building:
			tokens.append(token)
		cursor += 1

	if building:
		tokens.append(token)

	return tokens
