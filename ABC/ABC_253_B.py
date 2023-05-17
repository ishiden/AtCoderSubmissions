import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    p = []

    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                p.append([i, j])

    ans = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])

    print(ans)

if __name__ == '__main__':
    main()