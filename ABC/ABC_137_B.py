import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    K, X = map(int, input().split())
    start = max(-1000000, X - K + 1)
    end = min(1000000 + 1, X + K)
    for i in range(start, end):
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()