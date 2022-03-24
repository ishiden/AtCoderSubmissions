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
    highest = 0
    for _ in range(N):
        p = int(input())
        if highest < p:
            highest = p
        ans += p
    print(ans - (highest//2))

if __name__ == '__main__':
    main()