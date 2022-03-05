import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 1
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    cur = 0
    for i in range(N):
        cur += L[i]
        if cur > X:
            break
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()