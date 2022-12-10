import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    rs, cs, rt, ct = rs-1, cs-1, rt-1, ct-1
    S = [input() for _ in range(H)]

    inf = float('inf')
    A = [[inf] * W for _ in range(H)]

    A[rs][cs] = -1

    openpos = collections.deque()
    openpos.append((rs, cs))

    while (len(openpos) != 0):
        p = openpos.popleft()
        r, c = p[0], p[1]
        cnt = A[r][c] + 1

        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in D:
            rr = r
            cc = c
            while True:
                rr += d[0]
                cc += d[1]

                if (0 <= rr < H) and (0 <= cc < W):
                    if S[rr][cc] == '.' and A[rr][cc] > A[r][c]:
                        A[rr][cc] = cnt
                        openpos.append((rr, cc))
                    else:
                        break
                else:
                    break
    A[rs][cs] = 0

    print(A[rt][ct])

if __name__ == '__main__':
    main()