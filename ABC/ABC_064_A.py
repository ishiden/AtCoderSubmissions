import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    r, g, b = input().split()
    rgb = int(r + g + b)
    if rgb % 4 == 0:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()