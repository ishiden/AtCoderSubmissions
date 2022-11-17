import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    n, m = map(int, input().split())
    l = n%12 * 30 + m*0.5
    s = m*6
    ans = abs(l - s)
    if ans > 180:
        ans = 360 - ans
    print(ans)

if __name__ == '__main__':
    main()