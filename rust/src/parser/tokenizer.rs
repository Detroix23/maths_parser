//! # Python mathematics parser.
//! /src/structures/tokenizer.rs

use crate::structures::tokens;

pub struct Tokenizer {
	/// List of all `known` `Token`s.
	known: Vec<tokens::Token>,
}

impl Tokenizer {
	pub fn new(known: Vec<tokens::Token>) -> Tokenizer {
		Tokenizer { known }
	}

	/// Parse a given `expression` into a list of `Token`s.
	pub fn parse(expression: String) -> Vec<tokens::Token> {
		todo!()
	}
}