import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, Q = map(int, input().split())
    p = []
    maxX, maxY = 0, 0
    minX, minY = 10**10, 10**10
    for _ in range(N):
        x, y = map(int, input().split())
        x, y = x-y, x+y
        p.append([x, y])
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minX = min(minX, x)
        minY = min(minY, y)

    for _ in range(Q):
        q = int(input())
        q -= 1
        M = 0
        M = max(abs(maxX - p[q][0]), max(abs(maxY - p[q][1]), max(abs(minX - p[q][0]), abs(minY - p[q][1]))))
        print(M)

if __name__ == '__main__':
    main()