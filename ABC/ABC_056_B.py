import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    W, a, b = map(int, input().split())
    # if a < b:
    #     ans = b - (a + W)
    # else:
    #     ans = abs((b + W) - a)
    # if a <= b <= (a + W) or a <= (b + W) <= (a + W):
    #     ans = 0
    if abs(a - b) > W:
        ans = abs(a - b) - W
    print(ans)


if __name__ == '__main__':
    main()