import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 998244353
    ans = 0
    N, M, K = map(int, input().split())
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K):
            for k in range(1, M+1):
                if j + k <= K:
                    dp[i+1][j+k] += dp[i][j]%mod

    for i in range(K+1):
        ans += dp[-1][i]%mod

    print(ans%mod)

if __name__ == '__main__':
    main()