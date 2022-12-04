import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = -10**9
    N = int(input())
    S = list(map(int, input().split()))
    T = []
    for i in range(N):
        T.append([-10**9, -10**9])
        for j in range(N):
            if i == j:
                continue
            tmp_t = 0
            tmp_a = 0
            c = 0
            for k in  range(min(i, j), max(i+1, j+1)):
                if c%2 == 0:
                    tmp_t += S[k]
                else:
                    tmp_a += S[k]
                c += 1
            if tmp_a > T[i][1]:
                T[i] = [tmp_t, tmp_a]
        ans = max(ans, T[i][0])
    print(ans)

if __name__ == '__main__':
    main()