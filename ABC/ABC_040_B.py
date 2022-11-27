import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 10**9
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            ans = min(ans, (n - i * j) + abs(i - j))
    print(ans)

if __name__ == '__main__':
    main()