//! # Python mathematics parser.
//! /src/defaults/tokens.rs

use crate::modules::vec_string;
use crate::structures::tokens;

pub fn generate_operations() -> Vec<tokens::Token> {
	vec![
		tokens::Token::new(
			"Addition".to_string(),
			vec_string(&["+"]),
			tokens::TokenType::FUNCTION,
		),
		tokens::Token::new(
			"Subtraction".to_string(),
			vec_string(&["-"]),
			tokens::TokenType::FUNCTION,
		),
		tokens::Token::new(
			"Multiplication".to_string(),
			vec_string(&["*"]),
			tokens::TokenType::FUNCTION,
		),
		tokens::Token::new(
			"Division".to_string(),
			vec!["/".to_string()],
			tokens::TokenType::FUNCTION,
		),
		tokens::Token::new(
			"Exponentiation".to_string(),
			vec_string(&["^", "**"]),
			tokens::TokenType::FUNCTION,
		),
	]
}