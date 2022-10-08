import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 10**9 + 7
    N, L = map(int, input().split())
    dp = [0] * (N+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1]
        if 0 <= i-L:
            dp[i] += dp[i-L]
            dp[i] %= mod

    print(dp[N])

if __name__ == '__main__':
    main()