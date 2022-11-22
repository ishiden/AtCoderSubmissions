import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, Q = map(int, input().split())
    g = set()
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A, B = A - 1, B - 1
        if T == 1:
            g.add((A, B))
        elif T == 2 and (A, B) in g:
            g.remove((A, B))
        elif T == 3:
            if (A, B) in g and (B, A) in g:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()