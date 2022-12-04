import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    ans_str = 'Yes'
    H, W = map(int, input().split())
    A, B = [], []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    for _ in range(H):
        B.append(list(map(int, input().split())))
    for i in range(H-1):
        for j in range(W-1):
            d = B[i][j] - A[i][j]
            if d == 0:
                continue
            ans += abs(d)
            A[i][j] += d
            A[i+1][j] += d
            A[i][j+1] += d
            A[i+1][j+1] += d
    for i in range(H):
        if A[i][W-1] != B[i][W-1]:
            ans_str = 'No'
            break
    print(ans_str)
    if ans_str == 'Yes':
        print(ans)

if __name__ == '__main__':
    main()