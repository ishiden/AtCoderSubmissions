import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    N, Q = map(int, input().split())
    l = [i for i in range(1, N+1)]
    di = dict(zip(l, l))
    ds = di.copy()
    for _ in range(Q):
        x = int(input())
        if di[x] == N:
           left = ds[di[x]-1]
           ds[di[x]] = ds[di[x]-1]
           ds[di[x]-1] = x
           di[left] += 1
           di[x] -= 1

        else:
           right = ds[di[x]+1]
           ds[di[x]] = ds[di[x]+1]
           ds[di[x]+1] = x
           di[right] -= 1
           di[x] += 1
    for i in ds.values():
        ans += ' ' + str(i)
    print(str.lstrip(ans))

if __name__ == '__main__':
    main()