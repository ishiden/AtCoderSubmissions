import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans1 = 0
    ans2 = 0
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    setA = set(A)
    setB = set(B)
    for i in range(N):
        if A[i] == B[i]:
            ans1 += 1
        else:
            if A[i] in setB:
                ans2 += 1

    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()