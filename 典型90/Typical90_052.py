import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 10**9 + 7
    ans = 1
    N = int(input())
    for _ in range(N):
        ans *= sum(list(map(int, input().split())))%mod
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()