import sys
import bisect
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    A.sort()
    for _ in range(Q):
        B = int(input())
        temp = bisect.bisect_left(A, B)
        if temp == N:
            ans = abs(A[-1] - B)
        else:
            ans = min(abs(A[temp] - B), abs(A[temp-1]-B))
        print(ans)

if __name__ == '__main__':
    main()