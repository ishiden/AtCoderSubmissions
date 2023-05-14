import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = []
    N = int(input())
    A = list(map(int, input().split()))
    ans.append(A[0])
    for i in range(1, N):
        if abs(ans[-1] - A[i]) == 1:
            ans.append(A[i])
            continue
        if ans[-1] < A[i]:
            for j in range(ans[-1] + 1, A[i]+1):
                ans.append(j)
        else:
            tmp = []
            for j in range(A[i], ans[-1]):
                tmp.append(j)
            ans += reversed(tmp)
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()