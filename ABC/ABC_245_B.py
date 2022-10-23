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
    A.sort()
    if A[0] == 0:
        for i in range(1, N):
            if A[i] - A[i-1] > 1:
                ans = A[i-1] + 1
                break
        if ans == 0:
            ans = A[-1] + 1
    print(ans)

if __name__ == '__main__':
    main()