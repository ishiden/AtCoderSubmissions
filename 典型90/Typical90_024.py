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

    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    if diff > K or (K-diff)%2:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()