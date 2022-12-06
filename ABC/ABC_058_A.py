import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    a, b, c = map(int, input().split())
    if b - a == c - b:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()