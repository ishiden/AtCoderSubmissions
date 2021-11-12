import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, M = map(int, input().split())
    if N != M:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()