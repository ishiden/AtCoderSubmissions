import bisect
import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    C = [0] * (N+1)
    for i in range(2, N+1):
        if C[i] != 0:
            continue
        for j in range(i, N+1, i):
            C[j] += 1

    for i in range(N+1):
        if C[i] >= K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()