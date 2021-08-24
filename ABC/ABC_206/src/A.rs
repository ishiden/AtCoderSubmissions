use proconio::input;

fn main() {
    input!{
        n: i32,
    }
    let a: i32 = n * 108;
    let ans = {
        if a < 20600 {
            "Yay!"
        } else if a >= 20700 {
            ":("
        } else {
            "so-so"
        }
    };
    println!("{}", ans);
}
