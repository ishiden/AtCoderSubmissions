import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    f = [False] * N
    cur = X - 1
    while f[cur] == False:
        f[cur] = True
        cur = A[cur] - 1
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()