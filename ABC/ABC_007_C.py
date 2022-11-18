import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    m = [input().rstrip('\n') for _ in range(R)]
    q = collections.deque()
    q.append([sy, sx])
    dist = [[-1]*C for _ in range(R)]
    dist[sy][sx] = 0

    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while len(q) > 0:
        y, x = q.popleft()

        for dy, dx in dirc:
            y2 = y + dy
            x2 = x + dx

            if not (0 <= y2 < R and 0 <= x2 < C):
                continue
            if m[y2][x2] == '#':
                continue
            if dist[y2][x2] == -1:
                dist[y2][x2] = dist[y][x] + 1
                q.append([y2, x2])

    print(dist[gy][gx])

if __name__ == '__main__':
    main()