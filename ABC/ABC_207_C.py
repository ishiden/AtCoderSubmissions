import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    l = [0]*N
    r = [0]*N
    for i in range(N):
        t, l[i], r[i] = map(int, input().split())
        if t == 2:
            r[i] -= 0.5
        elif t == 3:
            l[i] += 0.5
        elif t == 4:
            l[i] += 0.5
            r[i] -= 0.5
    for i in range(N):
        for j in range(i+1, N):
            ans += (max(l[i], l[j]) <= min(r[i], r[j]))

    print(ans)

if __name__ == '__main__':
    main()