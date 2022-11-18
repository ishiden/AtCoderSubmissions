import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def dfs(n, k, t, q, v):
    if q == n:
        return v == 0
    for i in range(k):
        if dfs(n, k, t, q + 1, v^t[q][i]):
            return True
    return False

def main():
    ans = 'Nothing'
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    if dfs(N, K, T, 0, 0):
        ans = 'Found'
    print(ans)

if __name__ == '__main__':
    main()