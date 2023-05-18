import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 1000000007
    N, M = map(int, input().split())
    ng = [False] * N
    for _ in range(M):
        a = int(input())
        ng[a-1] = True
    dp = [0] * (N)
    dp[0] = 0 if ng[0] else 1
    if N > 1:
        dp[1] += 0 if ng[1] else dp[0] + 1
        for i in range(2, N):
            if ng[i]:
                continue
            dp[i] = dp[i-1]%mod + dp[i-2]%mod

    print(dp[-1]%mod)

if __name__ == '__main__':
    main()