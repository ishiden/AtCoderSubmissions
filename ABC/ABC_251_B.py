import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(0)
    set_w = set()
    for i in range(N):
        for j in range(i+1, N+2):
            for k in range(j+1, N+2):
                if A[i] + A[j] + A[k] <= W:
                    set_w.add(A[i] + A[j] + A[k])
    print(len(set_w))

if __name__ == '__main__':
    main()