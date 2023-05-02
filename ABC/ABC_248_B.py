import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B, K = map(int, input().split())
    while A < B:
        A *= K
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()