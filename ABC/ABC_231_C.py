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
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(Q):
        x = int(input())
        print(N - bisect.bisect_left(A, x))

if __name__ == '__main__':
    main()