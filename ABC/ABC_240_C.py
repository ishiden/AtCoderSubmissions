import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N, X = map(int, input().split())
    J = [[]]
    for i in range(N):
        a, b = map(int, input().split())
        J.append([a, b])
    dp = [[False] * (X+1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N+1):
        for j in range(X + 1):
            if not dp[i-1][j]:
                continue
            if j + J[i][0] <= X:
                dp[i][j + J[i][0]] = True
            if j + J[i][1] <= X:
                dp[i][j + J[i][1]] = True
    if dp[N][X]:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()