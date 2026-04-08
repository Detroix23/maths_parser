"""
# Python mathematics parser.
src/maths_parser_detroix23/parsing/parenthesis.py
"""

from maths_parser_detroix23.structures import types, tokens

def correct(token_list: types.Tokens) -> bool:
	"""
	Check if the parenthesis are well closed, correct, healthy.
	"""
	open_count: int = 0
	index: int = 0

	while index < len(token_list) and open_count >= 0:
		if token_list[index] == tokens.BLOCK_OPENING:
			open_count += 1
		elif token_list[index] == tokens.BLOCK_CLOSING:
			open_count -= 1

	return open_count == 0

def package(token_list: types.Tokens) -> tokens.Block:
    def package_in(token_list: types.Tokens, depth: int = 0) -> tuple[tokens.Block, int]:
        index: int = 0    
        in_block: bool = True
        expression: types.Tokens = []
        
        while in_block and index < len(token_list):
            if token_list[index] == tokens.BLOCK_OPENING:
                recurse = package_in(token_list[index + 1:], depth + 1)
                expression.append(recurse[0])
                index += recurse[1]
    
            elif token_list[index] == tokens.BLOCK_CLOSING:
                in_block = False
    
            else:
                expression.append(token_list[index])
                
            index += 1
    
        return (tokens.Block(expression, depth), index)

    return package_in(token_list, 0)[0]

