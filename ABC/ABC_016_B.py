import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = '!'
    A, B, C = map(int, input().split())
    if A - B == C and A + B == C:
        ans = '?'
    elif A + B == C:
        ans = '+'
    elif A - B == C:
        ans = '-'
    print(ans)

if __name__ == '__main__':
    main()