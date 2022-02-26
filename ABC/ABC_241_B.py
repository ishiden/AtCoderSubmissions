import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ac = collections.Counter(A)
    bc = collections.Counter(B)
    for b, c in bc.items():
        if ac[b] < c:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    main()