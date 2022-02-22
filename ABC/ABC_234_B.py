import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def f(X1, Y1, X2, Y2):
    return ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

def main():
    ans = 0
    N = int(input())
    p = []
    for i in range(N):
        x, y = map(int, input().split())
        p.append([x, y])
    for i in range(N-1):
        for j in range(i+1, N):
            ans = max(ans, f(p[i][0], p[i][1], p[j][0], p[j][1]))

    print(ans)

if __name__ == '__main__':
    main()