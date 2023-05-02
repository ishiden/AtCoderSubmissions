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
    v = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)
    for i in range(1, N+1):
        v[i].sort()
        if v[i][0] > i:
            continue
        if len(v[i]) == 1 or i < v[i][1]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()