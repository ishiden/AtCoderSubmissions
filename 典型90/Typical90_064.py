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
    A = list(map(int, input().split()))
    d = [0] * (N)
    for i in range(N-1):
        d[i] = A[i+1] - A[i]
        ans += abs(d[i])
    for _ in range(Q):
        L, R, V = map(int, input().split())
        L, R = L - 1, R - 1
        before = abs(d[L-1]) + abs(d[R])
        if L != 0:
            d[L-1] += V
        if R != N - 1:
            d[R] -= V
        after = abs(d[L-1]) + abs(d[R])
        ans += after - before
        print(ans)

if __name__ == '__main__':
    main()