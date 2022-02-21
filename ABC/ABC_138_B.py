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
    A = list(map(int, input().split()))
    c = 0
    for i in range(N):
        c += 1/A[i]
    ans = 1 / c

    print(ans)

if __name__ == '__main__':
    main()