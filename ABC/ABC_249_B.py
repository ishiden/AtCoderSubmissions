import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'No'
    S = input().rstrip('\n')
    if len(S) == len(set(S)):
        if S.upper() != S:
            if S.lower() != S:
                ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()