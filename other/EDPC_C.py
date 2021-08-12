import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    dp = []
    for i in range(N):
        a, b, c = map(int, input().split())
        dp.append([0, 0, 0])
        if i == 0:
            dp[i][0] = a
            dp[i][1] = b
            dp[i][2] = c
        else:
            dp[i][0] = max(dp[i-1][1] + a, dp[i-1][2] + a)
            dp[i][1] = max(dp[i-1][2] + b, dp[i-1][0] + b)
            dp[i][2] = max(dp[i-1][0] + c, dp[i-1][1] + c)
    print(max(dp[N-1][0], max(dp[N-1][1], dp[N-1][2])))

if __name__ == '__main__':
    main()