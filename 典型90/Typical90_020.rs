use std::convert::TryInto;
use proconio::input;

fn main() {
    input!{
        a : usize,
        b : usize,
        c : usize,
    }

    if a < c.pow(b.try_into().unwrap()) {
        println!("Yes");
    } else {
        println!("No");
    }
}