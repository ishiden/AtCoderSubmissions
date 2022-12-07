import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    ans = A + B
    if ans >= 10:
        ans = 'error'
    print(ans)

if __name__ == '__main__':
    main()