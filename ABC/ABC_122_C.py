import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    S = input().rstrip('\n')
    a = [0] * N
    for i in range(N-1):
        if S[i] != 'A':
            continue
        if S[i+1] != 'C':
            continue
        a[i] = 1
    s = [0] * N
    s[0] = a[0]
    for i in range(1, N):
        s[i] = s[i-1] + a[i]

    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ans = s[r-1]
        if l:
            ans -= s[l-1]
        print(ans)

if __name__ == '__main__':
    main()