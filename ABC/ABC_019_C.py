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
    a = set()
    for i in range(N):
        while A[i]%2 == 0 and A[i] != 0:
            A[i] /= 2
        a.add(A[i])

    print(len(a))

if __name__ == '__main__':
    main()