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
    A, B = map(int, input().split())
    d = (A**2 + B**2)**0.5
    print(A / d, B / d)

if __name__ == '__main__':
    main()