//! # Python mathematics parser.
//! /src/structures/tokens.rs

pub const DIGITS: [char; 10] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

pub const BLOCK_OPENING: [char; 3] = ['(', '[', '{'];
pub const BLOCK_CLOSING: [char; 3] = [')', ']', '}'];

/// # Differentiate `TokeType`s.
/// Finite set that compose an expression.
#[derive(Clone, Copy)]
pub enum TokenType {
	UNKNOWN,
	NUMBER,
	VARIABLE,
	/// Literal function name (_eg_: `f(x)`), or symbol expression (_eg_: `+`).
	FUNCTION,
	/// Block delimiter: all sort of parenthesis.
	DELIMITER,
}

/// # Shared `TokenCommon` proprieties.
pub trait TokenCommon {
	/// Get all `String` `representation`.
	fn get_representations(self: &Self) -> Vec<String>;

	fn get_token_type(self: &Self) -> TokenType;

}

#[derive(Clone)]
pub struct Token {
	name: String,
	representations: Vec<String>,
	token_type: TokenType,
}

impl Token {
	pub fn new(
		name: String, 
		representations: Vec<String>, 
		token_type: TokenType
	) -> Token {
		Token {
			name,
			representations,
			token_type,
		}
	}
}

impl TokenCommon for Token {
	fn get_representations(self: &Self) -> Vec<String> {
		self.representations.clone()
	}
	
	fn get_token_type(self: &Self) -> TokenType {
		self.token_type
	}
}