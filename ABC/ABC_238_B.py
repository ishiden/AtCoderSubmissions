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
    l = [False] * 360
    l[0] = True
    p = 0
    for i in range(N):
        p += A[i]
        p %= 360
        l[p] = True
    cur = 0
    for j in range(361):
        if l[j%360]:
            ans = max(ans, cur)
            cur = 0
        cur += 1

    print(ans)

if __name__ == '__main__':
    main()