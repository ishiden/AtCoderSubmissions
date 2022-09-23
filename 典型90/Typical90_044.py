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
    shift_cnt = 0
    for i in range(Q):
        T, x, y = map(int, input().split())
        x = x - 1 - shift_cnt
        y = y - 1 - shift_cnt

        if x < 0:
            x = N - abs(x)
        if y < 0:
            y = N - abs(y)

        if T == 1:
            A[x], A[y] = A[y], A[x]
        elif T == 2:
            shift_cnt += 1
        else:
            print(A[x])

if __name__ == '__main__':
    main()