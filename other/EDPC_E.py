import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    w, v = [], []
    max_v = 10**5 + 1
    inf = 10**9 + 1
    dp = [[inf]* max_v for i in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        x, y = map(int, input().split())
        w.append(x)
        v.append(y)
    for i in range(1, N + 1):
        for j in range(max_v):
            if j - v[i-1] >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]] + w[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    ans = max_v - 1
    while(dp[N][ans] > W):
        ans -= 1

    print(ans)

if __name__ == '__main__':
    main()