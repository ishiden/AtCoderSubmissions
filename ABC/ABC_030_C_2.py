import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def bisect_left(list, target, start, end):
    l = start
    r = end
    while l < r:
        mid = (l + r) // 2
        if list[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

def main():
    ans = 0
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    now_A = True
    a_idx = 0
    b_idx = 0
    arr_at = 0
    while b_idx < M:
        if now_A:
            if a_idx >= N or arr_at > A[a_idx]:
                break
            arr_at = A[a_idx] + X
            if arr_at > B[-1]:
                break
            b_idx = bisect_left(B, arr_at, b_idx, M-1)
            a_idx += 1
        else:
            arr_at = B[b_idx] + Y
            a_idx = bisect_left(A, arr_at, a_idx, N-1)
            b_idx += 1
            ans += 1
        now_A = not now_A

    print(ans)

if __name__ == '__main__':
    main()