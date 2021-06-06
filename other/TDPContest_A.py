import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    M = max(P)
    dp = [[0] * (N * M + 1) for i in range(N + 1)]
    dp[0][0] = 1
    for i, a in enumerate(P):
        for j in range(N * M + 1):
            dp[i+1][j] = dp[i][j]
            if j >= a:
                dp[i+1][j] |= dp[i][j-a]
    print(sum(dp[N]))

if __name__ == '__main__':
    main()