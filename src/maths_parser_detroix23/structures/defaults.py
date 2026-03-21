"""
# Python mathematics parser.
src/maths_parser_detroix23/structures/defaults.py
"""

from typing import Final

PARENTHESIS: Final[set[str]] = {"(", ")"}
"""Both block closing and opening characters."""

OPERATORS: Final[set[str]] = {"+", "-", "*", "/", "^", "**"}
"""All supported and linked operators."""

NUMBER_SYMBOLS: Final[set[str]] = {".", ",", "_"}

SPACE: Final[set[str]] = {" ", "\n", "\r"}
"""Breaks, whitespaces."""

UNKNOWN_TOKEN: Final[str] = "?"
