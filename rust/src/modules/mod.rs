//! # Python mathematics parser.
//! /src/modules/mod.rs

pub fn vec_string(strings: &[&str]) -> Vec<String> {
	strings
		.iter()
		.map(|s| s.to_string())
		.collect()
}