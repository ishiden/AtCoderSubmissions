import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input().rstrip('\n'))
    for s in reversed(S):
        print(s)

if __name__ == '__main__':
    main()