import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 0
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    d = [0] * N
    for i in range(N):
        k = min(K, A[i]//X)
        K -= k
        ans += max(0, A[i] - (k * X))
        d[i] = A[i]%X
    if K > 0:
        d.sort(reverse=True)
        for i in range(N):
            ans -= d[i]
            K -= 1
            if K == 0:
                break
    print(ans)

if __name__ == '__main__':
    main()