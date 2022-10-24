import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x, y = x1, y1
    if x1 == x2:
        x = x3
    elif x1 == x3:
        x = x2
    if y1 == y2:
        y = y3
    elif y1 == y3:
        y = y2
    print(x, y)

if __name__ == '__main__':
    main()