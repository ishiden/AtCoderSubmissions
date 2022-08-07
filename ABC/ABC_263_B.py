import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 1
    N = int(input())
    P = [0] + list(map(int, input().split()))
    idx = P[-1] - 1
    while idx != 0:
        idx = P[idx] - 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()