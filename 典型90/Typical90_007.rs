use proconio::{input, fastout};
use std::cmp::min;

#[fastout]
fn main() {
  input!{
    n: usize,
    mut a: [isize; n],
    q: usize,
    b: [isize; q]
  }
  a.push(std::isize::MIN);
  a.push(std::isize::MAX);
  a.sort();
  a.dedup();

  for r in b {
    let idx = a.binary_search(&r).unwrap_or_else(|x| x);
    let ans = min((a[idx]-r).abs(), (a[idx-1]-r).abs());
    println!("{}", ans);
  }
}