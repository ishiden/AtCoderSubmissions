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
    c = collections.Counter(A)
    for i in range(N):
        if c[i + 1] != 4:
            ans = i + 1
            break

    print(ans)

if __name__ == '__main__':
    main()