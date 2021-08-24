use proconio::input;

fn main() {
    input!{
        n: usize,
        q: usize,
        a: [usize; n],
        k: [usize; q],
    };

    for i in k {
        if i < a[0] {
            println!("{}", i);
            continue;
        }
        let mut l = 0;
        let mut r = n;
        while r - l > 1 {
            let m = (l + r) / 2;
            if a[m] < i + m + 1 {
                l = m;
            } else {
                r = m;
            }
        }
        let ans = i + l + 1;
        println!("{}", ans);
    }
}
