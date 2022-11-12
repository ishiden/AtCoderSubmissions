import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    s = set()
    for _ in range(N):
        a = int(input())
        if a in s:
            ans += 1
        else:
            s.add(a)
    print(ans)

if __name__ == '__main__':
    main()