import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 1000 * 11
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    M = int(input())
    R = []
    for _ in range(M):
        R.append(list(map(int, input().split())))
    P = itertools.permutations(list(range(N)), N)

    C = [[False]* N for _ in range(N)]
    for i in range(M):
        x, y = R[i][0]-1, R[i][1]-1
        C[x][y] = True
        C[y][x] = True

    for pattern in P:
        temp = A[pattern[0]][0]
        d = False
        for i in range(1, N):
            if not C[pattern[i-1]][pattern[i]]:
                temp += A[pattern[i]][i]
            else:
                d = True
                break
        if not d:
            ans = min(temp, ans)

    if ans != 1000*11:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()