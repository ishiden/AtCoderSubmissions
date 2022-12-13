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
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = sum(L[:K])
    print(ans)

if __name__ == '__main__':
    main()