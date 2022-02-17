import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    for h in H:
        if h >= K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()