import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    l = []
    for _ in range(H):
        l.append(list(map(int, input().split())))
    for i1 in range(H):
        for i2 in range(i1, H):
            for j1 in range(W):
                for j2 in range(j1, W):
                    if (l[i1][j1] + l[i2][j2] > l[i2][j1] + l[i1][j2]):
                        print('No')
                        exit()
    print('Yes')

if __name__ == '__main__':
    main()