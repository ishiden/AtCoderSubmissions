use proconio::input;

fn gcd(x: usize, y:usize) -> usize{
    if y == 0 {
        return x
    } else {
        gcd(y, x%y)
    }
}

fn main() {
    input!{
        a : usize,
        b : usize,
        c : usize
    }

    let g = gcd(gcd(a, b), gcd(b, c));
    println!("{}", (a/g + b/g + c/g) - 3);
}