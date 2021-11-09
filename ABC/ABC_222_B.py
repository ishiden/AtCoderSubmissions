import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        if a < P:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()