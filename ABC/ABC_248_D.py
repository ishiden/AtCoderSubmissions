import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    idx = [[] for _ in range(N)]
    for i in range(N):
        idx[A[i]-1].append(i)

    for i in range(Q):
        L, R, X = map(int, input().split())
        st = bisect.bisect_left(idx[X-1], L-1)
        gl = bisect.bisect_right(idx[X-1], R-1)
        print(gl - st)

if __name__ == '__main__':
    main()