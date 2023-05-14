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
    X, t = map(int, input().split())
    ans = max(0, X - t)
    print(ans)

if __name__ == '__main__':
    main()