import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'A'
    x, a, b = map(int, input().split())
    if abs(b - x) < abs(a - x):
        ans = 'B'

    print(ans)

if __name__ == '__main__':
    main()