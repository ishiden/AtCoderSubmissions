import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(1, N+1):
        Q[P[i-1]-1] = i
    print(' '.join(map(str, Q)))

if __name__ == '__main__':
    main()