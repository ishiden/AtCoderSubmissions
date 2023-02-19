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
    S = input().rstrip('\n')
    a, b = [0]*(N+1), [0]*(N+1)
    for i in range(N):
        if S[i] == 'o':
            a[i+1] = i+1
            b[i+1] = b[i]
        else:
            a[i+1] = a[i]
            b[i+1] = i+1
    for i in range(N+1):
        ans += min(a[i], b[i])

    print(ans)

if __name__ == '__main__':
    main()