import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    S = list(input().rstrip('\n') * 6)
    print(''.join(S[:6]))

if __name__ == '__main__':
    main()