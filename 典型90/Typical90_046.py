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
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    transA, transB, transC = [0]*46, [0]*46, [0]*46
    for i in range(N):
        transA[A[i]%46] += 1
        transB[B[i]%46] += 1
        transC[C[i]%46] += 1

    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k)%46 == 0:
                    ans += transA[i] * transB[j] * transC[k]

    print(ans)

if __name__ == '__main__':
    main()