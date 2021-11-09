import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    mod = 10**9 + 7
    N = int(input())
    S = input().rstrip('\n')
    t = 'atcoder'
    lt = len(t)
    dp = [[0] * (lt+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1

    for i in range(N):
        for j in range(lt):
            if S[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                dp[i+1][j+1] %= mod
            else:
                dp[i+1][j+1] = dp[i][j+1]
                dp[i+1][j+1] %= mod


    print(ans)

if __name__ == '__main__':
    main()