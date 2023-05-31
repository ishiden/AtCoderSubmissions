import bisect
import collections
import itertools
import math
import re
import sys
import heapq
from enum import Enum

input = sys.stdin.readline

class te(Enum):
    G = 1
    C = 2
    P = 3

telist = 'PGCPG'

def janken(p1, p2):
    p1v = te[p1].value
    if p1 == p2:
        return 0
    if telist[p1v+1] == p2:
        return 1
    if telist[p1v-1] == p2:
        return 2

def main():
    N, M = map(int, input().split())
    players = [[i, 0] for i in range(2*N)]
    t = []
    for _ in range(N*2):
        t.append(input().rstrip('\n'))

    res = input().rstrip('\n')
    for i in range(M):
        for j in range(0, N*2, 2):
            r = janken(t[players[j][0]][i], t[players[j+1][0]][i])
            if r == 1:
                players[j][1] += 1
            elif r == 2:
                players[j+1][1] += 1
        players.sort(key=lambda x: x[0])
        players.sort(key=lambda x: x[1], reverse=True)
    for p in players:
        print(p[0]+1)

if __name__ == '__main__':
    main()