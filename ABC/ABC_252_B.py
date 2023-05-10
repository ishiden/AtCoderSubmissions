import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = set(map(int, input().split()))
    target = max(A)
    for i in range(N):
        if A[i] == target:
            if (i+1) in B:
                ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()