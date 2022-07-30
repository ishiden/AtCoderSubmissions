import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

sys.setrecursionlimit(10**5+1)

def dfs(n, l, g):
    t = l[n]
    for i in range(len(t)):
        if g[t[i]] != 0:
            continue
        g[t[i]] = -1 * g[n]
        dfs(t[i], l, g)

def main():
    ans = 0
    N = int(input())
    l = []
    for i in range(N):
        l.append([])
    for _ in range(N-1):
        A, B = map(int, input().split())
        l[A-1].append(B-1)
        l[B-1].append(A-1)

    g = [0] * N
    g[0] = -1

    dfs(0, l, g)

    r, w = [], []
    for i in range(N):
        if g[i] == -1:
            r.append(i+1)
        else:
            w.append(i+1)

    ans_l = r if len(r) > len(w) else w

    for i in range(N//2):
        print(ans_l[i], end=' ')
    print('')

if __name__ == '__main__':
    main()