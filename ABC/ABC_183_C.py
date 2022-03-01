import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    P = itertools.permutations(range(1, N), N-1)
    for pl in P:
        temp = T[0][pl[0]]
        for i in range(1, N-1):
            temp += T[pl[i-1]][pl[i]]
        temp += T[pl[-1]][0]
        if temp == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()