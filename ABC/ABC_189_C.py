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
    N = int(input())
    A = list(map(int, input().split()))
    for l in range(N):
        m = A[l]
        for r in range(l, N):
            m = min(m, A[r])
            ans = max(ans, m*(r-l+1))

    print(ans)

if __name__ == '__main__':
    main()