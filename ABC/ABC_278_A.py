import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N < K:
        ans = [0] * N
    else:
        ans = A[K:] + [0] * K
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()