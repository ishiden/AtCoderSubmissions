use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    let mut a: Vec<i32> = vec![0; n+1];
    let mut b: Vec<i32> = vec![0; n+1];

    for i in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();

        let c: i32 = iter.next().unwrap().parse().unwrap();
        let p: i32 = iter.next().unwrap().parse().unwrap();

        a[i+1] = a[i];
        b[i+1] = b[i];

        if c == 1 {
            a[i+1] += p;
        } else {
            b[i+1] += p;
        }

    }

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let q: usize = input.trim().parse().unwrap();

    for _i in 0..q {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();

        let l: usize = iter.next().unwrap().parse().unwrap();
        let r: usize = iter.next().unwrap().parse().unwrap();

        println!("{} {}", a[r]-a[l-1], b[r]-b[l-1]);
    }
}