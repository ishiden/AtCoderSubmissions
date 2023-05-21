import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    okA = [False] * N
    okB = [False] * N
    okA[0] = True
    okB[0] = True
    for i in range(1, N):
        if okA[i-1]:
            if abs(A[i-1] - A[i]) <= K:
                okA[i] = True
            if abs(A[i-1] - B[i]) <= K:
                okB[i] = True
        if okB[i-1]:
            if abs(B[i-1] - A[i]) <= K:
                okA[i] = True
            if abs(B[i-1] - B[i]) <= K:
                okB[i] = True
        if not okA[i] and not okB[i]:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()