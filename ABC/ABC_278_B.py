import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def judge(h, m):
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    return 0 <= int(h[0] + m[0]) <= 23 and 0 <= int(h[1] + m[1]) <= 59

def main():
    ans = [0, 0]
    H, M = map(int, input().split())
    T = []
    for i in range(24):
        for j in range(60):
            if judge(i, j):
                T.append([i, j])
    for t in T:
        if (t[0] == H and t[1] >= M) or (t[0] > H):
                ans = t
                break
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()