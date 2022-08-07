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
    l.sort()
    for i in l:
        s = list(map(str, i))
        print(' '.join(s))

if __name__ == '__main__':
    main()