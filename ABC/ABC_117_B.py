import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    L = list(map(int, input().split()))
    maxEdge = max(L)
    if maxEdge < (sum(L) - maxEdge):
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()