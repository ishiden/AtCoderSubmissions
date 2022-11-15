import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    ans = 0
    L = int(input())
    print(combinations_count(L-1, 11))

if __name__ == '__main__':
    main()