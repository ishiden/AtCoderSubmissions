import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    d = collections.defaultdict(list)
    for i in range(N):
        d[A[i]].append(i+1)
    for _ in range(Q):
        x, k = map(int, input().split())
        if k <= len(d[x]):
            print(d[x][k-1])
        else:
            print(-1)

if __name__ == '__main__':
    main()