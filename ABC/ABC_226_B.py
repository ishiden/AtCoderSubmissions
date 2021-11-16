import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = set()
    N = int(input())
    for _ in range(N):
        ans.add(input())

    print(len(ans))

if __name__ == '__main__':
    main()