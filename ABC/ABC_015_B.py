import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    bugs = 0
    cnt = 0
    for a in A:
        if a == 0:
            continue
        bugs += a
        cnt += 1
    ans = math.ceil(bugs / cnt)

    print(ans)

if __name__ == '__main__':
    main()