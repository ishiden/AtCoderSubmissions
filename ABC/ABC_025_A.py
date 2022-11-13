import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    S = list(input().rstrip('\n'))
    N = int(input())
    S.sort()
    cnt = 0
    for s in S:
        for t in S:
            cnt += 1
            if cnt == N:
                print(s+t)
                exit()

if __name__ == '__main__':
    main()