import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'TAKAHASHI'
    A, B, C, D = map(int, input().split())
    if B/A < D/C:
        ans = 'AOKI'
    elif B/A == D/C:
        ans = 'DRAW'
    print(ans)

if __name__ == '__main__':
    main()