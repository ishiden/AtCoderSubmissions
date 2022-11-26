import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    for i in range(1, N+1):
        if len(G[i]) == 0:
            continue
        G[i].sort()
        if G[i][0] >= i:
            continue
        if len(G[i]) == 1:
            if G[i][0] < i:
                ans += 1
        elif G[i][0] < i and G[i][1] >= i:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()