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
    H = list(map(int, input().split()))
    cur = 0
    for i in range(N):
        if cur <= H[i]:
            ans += 1
            cur = H[i]
    print(ans)

if __name__ == '__main__':
    main()