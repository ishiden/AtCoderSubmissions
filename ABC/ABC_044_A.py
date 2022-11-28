import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    ans = min(N, K) * X + max(0, N - K) * Y

    print(ans)

if __name__ == '__main__':
    main()