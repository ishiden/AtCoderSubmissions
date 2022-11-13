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
    R = list(map(int, input().split()))
    R.sort()
    for r in R[N-K:]:
        ans = (ans + r) / 2
    print(ans)

if __name__ == '__main__':
    main()