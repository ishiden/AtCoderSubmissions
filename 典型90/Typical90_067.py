import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def convert(s):
    s = str(s)
    ten = 0
    x = 1
    for i in reversed(range(len(s))):
        ten += int(s[i]) * x
        x *= 8
    nine = ''
    while ten > 0:
        c = ten % 9
        if c == 8:
            c = 5
        nine = str(c) + nine
        ten //= 9
    return nine

def main():
    ans = 0
    N, K = map(int, input().split())
    if N != 0:
        for _ in range(K):
            N = convert(N)

    print(N)

if __name__ == '__main__':
    main()