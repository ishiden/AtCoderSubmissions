import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = ''
    t = 'abcdefghijklmnopqrstuvwxyz'
    P = list(map(int, input().split()))
    for p in P:
        ans += t[p-1]

    print(ans)

if __name__ == '__main__':
    main()