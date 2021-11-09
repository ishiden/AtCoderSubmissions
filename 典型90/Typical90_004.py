import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    t = []
    sr = [0]*H
    sc = [0]*W
    for i in range(H):
        t.append(list(map(int, input().split())))
        for j in range(W):
            sr[i] += t[-1][j]
            sc[j] += t[-1][j]
    for i in range(H):
        for j in range(W):
            t[i][j] = str(sr[i] + sc[j] - t[i][j])
        print(' '.join(t[i]))

if __name__ == '__main__':
    main()