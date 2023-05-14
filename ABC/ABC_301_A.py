import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    a, t = 0, 0
    ans = 'T'
    N = int(input())
    S = input().rstrip('\n')
    for i in range(N):
        if S[i] == 'A':
            a += 1
        else:
            t += 1
    if a > t:
        ans = 'A'
    elif a == t:
        if S[-1] == 'T':
            ans = 'A'

    print(ans)

if __name__ == '__main__':
    main()