import collections
import copy
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

angle_H = [-1, 0, 1, 0]
angle_W = [0, 1, 0, -1]

def disable_area(c, x, y, H, W):
    if c[x][y] == '#':
        return True
    cnt = 0
    for i in range(4):
        next_x = x + angle_H[i]
        next_y = y + angle_W[i]

        if next_x < 0 or H <= next_x:
            continue
        if next_y < 0 or W <= next_y:
            continue
        if c[next_x][next_y] == '.':
            cnt += 1
    return cnt < 2

def recursion(v, baseX, baseY, x, y, cnt, H, W):
    if x < 0 or H <= x:
        return -1
    if y < 0 or W <= y:
        return -1

    if baseX == x and baseY == y and cnt > 3:
        return cnt
    if v[x][y]:
        return -1

    ret = -1
    v[x][y] = True
    cnt += 1
    for i in range(4):
        t = copy.deepcopy(v)
        ret = max(ret, recursion(t, baseX, baseY, x + angle_H[i], y + angle_W[i], cnt, H, W))

    return ret

def main():
    ans = -1
    H, W = map(int, input().split())
    c = [input().rstrip('\n') for _ in range(H)]

    n = [[False for _ in range(W)]for _ in range(H)]
    for i in range(H):
        for j in range(W):
            n[i][j] = disable_area(c, i, j, H, W)

    for i in range(H):
        for j in range(W):
            v = copy.deepcopy(n)
            ans = max(ans, recursion(v, i, j, i, j, 0, H, W))
    print(ans)

if __name__ == '__main__':
    main()