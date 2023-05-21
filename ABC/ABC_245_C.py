import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    now = [A[0], B[0]]
    for i in range(1, N):
        tmp = [-1, -1]
        for n in now:
            if n == -1:
                continue
            if abs(n-A[i]) <= K:
                tmp[0] = A[i]
            if abs(n-B[i]) <= K:
                tmp[1] = B[i]
        if sum(tmp) == -2:
            ans = 'No'
            break
        now = tmp
    print(ans)

if __name__ == '__main__':
    main()