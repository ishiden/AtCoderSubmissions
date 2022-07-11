use proconio::input;
use std::cmp;

fn main() {
    input!{
        n : isize,
        a : isize,
        b : isize,
        c : isize
    }

    let mut ans : isize = 10000;
    let mut temp1 : isize = 0;
    let mut temp2 : isize = 0;

    for i in 0..10000 {
        for j in 0..10000 {
            temp1 = (n - a*i - b*j)%c;
            temp2 = (n - a*i - b*j)/c;
            if temp1 == 0 && temp2 <= (9999 - i - j) && temp2 >=0 {
                ans = cmp::min(ans, temp2 + i + j);
            }
        }
    }

    println!("{}", ans);
}