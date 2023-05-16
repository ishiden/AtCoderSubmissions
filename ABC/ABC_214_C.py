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
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    cur = T[0]
    for i in range(1, N):
        cur = min(T[i], cur + S[i-1])

    cur = min(cur + S[-1], T[0])
    print(cur)
    for i in range(1, N):
        cur = min(T[i], cur + S[i-1])
        print(cur)

if __name__ == '__main__':
    main()