import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    d = [10**9] * N
    d[0] = 0
    for i in range(1, N):
        d[i] = d[i - 1] + abs(A[i] - A[i-1])
        if i > 1:
            d[i] = min(d[i], d[i-2] + abs(A[i] - A[i-2]))
    print(d[N-1])

if __name__ == '__main__':
    main()