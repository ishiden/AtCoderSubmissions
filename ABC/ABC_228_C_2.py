import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(sum(map(int, input().split())))
    score = sorted(P, reverse=True)
    for i in range(N):
        ans = 'Yes' if P[i] + 300 >= score[K-1] else 'No'
        print(ans)

if __name__ == '__main__':
    main()