use proconio::input;

fn main() {
    input!{
        n: usize,
        s_i: Strings
    }

    let s: Vec<char> = s_i.chars().collect();

    let s_a: String = "atcoder".to_string();
    let a: Vec<char> = s_a.chars().collect();


    let mut dp = vec![vec![0; n+1]; 8];
    dp[0] = vec![1; n+1];
    for i in 0..7 {
        for j in 1..(n + 1) {
            dp[i+1][j] += dp[i+1][j-1];
            if s[j-1] == a[i] {
                dp[i+1][j] += dp[i][j-1];
            }
            dp[i+1][j] = dp[i+1][j] % 1000000007;
        }
    }
    println!("{}", dp[7][n]);
}