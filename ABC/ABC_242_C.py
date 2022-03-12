import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 998244353
    N = int(input())
    dp = [[0] * 9 for _ in range(N)]
    for i in range(9):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(9):
            dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            if j < 8:
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= mod
    print(sum(dp[-1])%mod)

if __name__ == '__main__':
    main()