import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(g, used, v):
    if used[v]:
        return
    used[v] = True
    for vv in g[v]:
        dfs(g, used, vv)

def main():
    ans = 0
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        g[A-1].append(B-1)
    for i in range(N):
        used = [False for _ in range(N)]
        dfs(g, used, i)
        ans += sum(used)

    print(ans)

if __name__ == '__main__':
    main()