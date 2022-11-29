import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    mod = 10**9 + 7
    N, K = map(int, input().split())
    if N == 1:
        ans = K
    else:
        ans = K * (K-1) * pow(K-2, N-2, mod)

    print(ans%mod)


if __name__ == '__main__':
    main()