import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(1, N):
        g = x - (A[i-1] + A[i])
        if g < 0:
            ans += abs(g)
            A[i] = max(0, A[i] + g)

    print(ans)

if __name__ == '__main__':
    main()