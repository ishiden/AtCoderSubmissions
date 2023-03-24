import collections
import itertools
import math
import re
import sys
import statistics
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    X, Y = 0, 0
    points_x = []
    points_y = []
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
        points_x.append(x)
        points_y.append(y)
    points_x.sort
    points_y.sort
    e = [statistics.median(points_x), statistics.median(points_y)]
    for p in points:
        ans += abs(p[0] - e[0]) + abs(p[1] - e[1])

    print(int(ans))

if __name__ == '__main__':
    main()