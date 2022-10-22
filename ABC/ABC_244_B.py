import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = [0, 0]
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    N = int(input())
    T = input().rstrip('\n')
    p = d[0]
    for t in T:
        if t == "S":
            ans = [ans[0] + p[0], ans[1] + p[1]]
        else:
            p = d[(d.index(p) + 1)%4]
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()