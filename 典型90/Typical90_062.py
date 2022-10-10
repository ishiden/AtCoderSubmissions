import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    d = collections.deque()
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            d.appendleft(x)
        elif t == 2:
            d.append(x)
        else:
            print(d[x-1])

if __name__ == '__main__':
    main()