import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    N = int(input())
    A = []
    first = 0
    second = 0
    for i in range(N):
        A.append(int(input()))
        if A[-1] >= first:
            second = first
            first = A[-1]
        elif A[-1] > second:
            second = A[-1]
    for i in range(N):
        if A[i] == first:
            ans += str(second) + '\n'
        else:
            ans += str(first) + '\n'
    print(ans)

if __name__ == '__main__':
    main()