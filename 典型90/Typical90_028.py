import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    area = [[0] * 1001 for _ in range(1001)]

    N = int(input())
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        area[lx][ly] += 1
        area[rx][ry] += 1
        area[lx][ry] -= 1
        area[rx][ly] -= 1

    for i in range(1001):
        for j in range(1, 1001):
            area[i][j] += area[i][j-1]

    for i in range(1, 1001):
        for j in range(1001):
            area[i][j] += area[i-1][j]

    ans = [0] * (N+1)
    for i in range(1001):
        for j in range(1001):
            ans[area[i][j]] += 1

    for i in range(1, N+1):
        print(ans[i])

if __name__ == '__main__':
    main()