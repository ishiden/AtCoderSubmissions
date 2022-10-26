import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    W = list(map(int, input().split()))
    l = sum(W)
    r = 0
    ans = l
    for i in range(N):
        l -= W[i]
        r += W[i]
        ans = min(ans, abs(l - r))

    print(ans)

if __name__ == '__main__':
    main()