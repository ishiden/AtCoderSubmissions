use proconio::input;

fn main() {
    input!{
        n : usize,
        mut a : [isize; n],
        mut b : [isize; n]
    }

    let mut ans : isize = 0;

    a.sort();
    b.sort();

    for i in 0..n {
        ans += (a[i] - b[i]).abs();
    }

    println!("{}", ans);
}