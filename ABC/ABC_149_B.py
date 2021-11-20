import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    A, B, K = map(int, input().split())
    a = max(A - K, 0)
    K = max(K - A, 0)
    B = max(B - K, 0)

    print(a, B)

if __name__ == '__main__':
    main()