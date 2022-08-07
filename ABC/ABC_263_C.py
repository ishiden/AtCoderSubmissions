import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    l = list(itertools.combinations(range(1, M+1), N))
    for i in l:
        print(*i, sep=' ')

if __name__ == '__main__':
    main()