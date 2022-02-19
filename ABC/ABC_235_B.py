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
    for i in range(1, N):
        if H[i-1] >= H[i]:
            ans = H[i-1]
            break
    if ans == 0:
        ans = H[N-1]
    print(ans)

if __name__ == '__main__':
    main()