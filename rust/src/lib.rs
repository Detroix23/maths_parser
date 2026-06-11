//! # Python mathematics parser.
//! /src/lib.rs
//! 
//! Mathematics parser: convert string expressions to 
//! an object tree of machine-readable operations.

mod modules;
mod structures;
mod basic;
mod parser;

#[cfg(test)]
mod tests {
    #[test]
    fn test1() -> () {
    }
}
