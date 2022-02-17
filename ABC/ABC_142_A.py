import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    if N % 2 == 0:
        ans = 0.5
    else:
        ans = (N//2 + 1) / N
    print(ans)

if __name__ == '__main__':
    main()