import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    mod = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1
    for i in range(N-1):
        for j in range(10):
            dp[i+1][(j+A[i+1])%10] += dp[i][j]
            dp[i+1][(j*A[i+1])%10] += dp[i][j]
            dp[i+1][(j+A[i+1])%10] %= mod
            dp[i+1][(j*A[i+1])%10] %= mod
    for i in range(10):
        print(dp[-1][i]%mod)

if __name__ == '__main__':
    main()