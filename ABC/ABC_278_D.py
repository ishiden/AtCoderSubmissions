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
    d = collections.defaultdict(int)
    for i in range(N):
        d[i] = A[i]
    b = 0
    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            d.clear()
            b = q[1]
        elif q[0] == 2:
            if bool(d[q[1]-1]):
                d[q[1]-1] += q[2]
            else:
                d[q[1]-1] = b + q[2]
        else:
            print(d[q[1]-1] if bool(d[q[1]-1]) else b)


if __name__ == '__main__':
    main()