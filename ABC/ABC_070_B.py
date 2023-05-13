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
    A, B, C, D = map(int, input().split())
    ans = min(B, D) - max(A, C)
    print(max(ans, 0))

if __name__ == '__main__':
    main()