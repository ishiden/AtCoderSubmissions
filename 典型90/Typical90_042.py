import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 10**9 + 7
    K = int(input())
    if K%9 != 0:
        print(0)
        exit()
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(K+1):
        b = min(i, 9)
        for j in range(1, b+1):
            dp[i] += dp[i-j]
            dp[i] %= mod

    print(dp[K])

if __name__ == '__main__':
    main()