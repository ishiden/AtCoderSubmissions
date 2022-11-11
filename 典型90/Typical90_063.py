import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    P = list()
    for i in range(H):
        P.append(list(map(int, input().split())))
    for i in range(1, 2**H+1):
        temp = []
        for j in range(H):
            if i >> j & 1:
                temp.append(P[j])
        d = collections.defaultdict(int)
        for k in range(W):
            allMatch = True
            for l in range(1, len(temp)):
                #前行と違ったら次の列にいく
                if temp[l-1][k] != temp[l][k]:
                    allMatch = False
                    break
            if len(temp) > 0 and allMatch:
                d[temp[0][k]] += len(temp)
        if any(d):
            ans = max(ans, max(d.values()))

    print(ans)

if __name__ == '__main__':
    main()