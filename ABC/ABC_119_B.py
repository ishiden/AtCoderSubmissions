import collections
import itertools
import math
import re
import sys
import heapq
from tokenize import Double

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for _ in range(N):
        x, y = input().split()
        x = float(x)
        if y == 'BTC':
            x *= 380000
        ans += x
    print(ans)

if __name__ == '__main__':
    main()