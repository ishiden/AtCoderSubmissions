import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C = map(int, input().split())
    ans = C - (A - B)
    print(max(ans, 0))

if __name__ == '__main__':
    main()