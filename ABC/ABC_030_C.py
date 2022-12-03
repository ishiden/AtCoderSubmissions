import collections
import itertools
import math
import re
import sys
import bisect
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    now_A = True
    a_idx = 0
    b_idx = 0
    while True:
        arr_at = -1
        if now_A:
            if a_idx >= N:
                break
            arr_at = A[a_idx] + X
            if B[-1] < arr_at:
                break
            b_idx = bisect.bisect_left(B, arr_at)
            now_A = False
        else:
            arr_at = B[b_idx] + Y
            a_idx = bisect.bisect_left(A, arr_at)
            now_A = True
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()