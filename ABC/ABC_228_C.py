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
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        total = sum(list(map(int, input().split())))
        P.append(total)
    score = sorted(P)
    for i in range(N):
        r = bisect.bisect_right(score, P[i]+300)
        ans = 'Yes' if r >= (N - K + 1) else 'No'
        print(ans)

if __name__ == '__main__':
    main()