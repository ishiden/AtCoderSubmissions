import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    c = 0
    A, B, K = map(int, input().split())
    for i in reversed(range(1, 101)):
        if A%i == 0 and B%i == 0:
            c += 1
            if c == K:
                ans = i
                break
    print(ans)

if __name__ == '__main__':
    main()