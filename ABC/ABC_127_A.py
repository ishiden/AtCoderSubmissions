import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    if A >= 13:
        ans = B
    elif A >= 6:
        ans = B // 2
    print(ans)

if __name__ == '__main__':
    main()