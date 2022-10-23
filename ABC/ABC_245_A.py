import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Takahashi'
    A, B, C, D = map(int, input().split())
    if A > C:
        ans = 'Aoki'
    elif A == C:
        if B > D:
            ans = 'Aoki'

    print(ans)

if __name__ == '__main__':
    main()