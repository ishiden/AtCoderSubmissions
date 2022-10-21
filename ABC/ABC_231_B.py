import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    d = collections.defaultdict(int)
    for _ in range(N):
        s = input().rstrip('\n')
        d[s] += 1

    print(max((v, k) for k, v in d.items())[1])

if __name__ == '__main__':
    main()