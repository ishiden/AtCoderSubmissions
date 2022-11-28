import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    g = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A, B = A-1, B-1
        g[A].add(B)
        G[A].append(B)
        g[B].add(A)
        G[B].append(A)
    for i in range(N):
        ans = set()
        for f in G[i]:
            for ff in G[f]:
                if ff !=  i and ff not in g[i]:
                    ans.add(ff)
        print(len(ans))

if __name__ == '__main__':
    main()