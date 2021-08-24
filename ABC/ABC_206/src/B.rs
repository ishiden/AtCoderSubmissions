use proconio::input;

fn main() {
    input!{
        mut n: i64,
    }

    let mut ans = 0;

    for i in 1..=n {
        n -= i;
        if n <= 0 {
            ans = i;
            break
        }
    }

    println!("{}", ans);
}
