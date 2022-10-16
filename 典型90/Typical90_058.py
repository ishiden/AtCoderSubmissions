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
    s = set()
    l = []
    x = N
    break_pos = -1
    cycle_start_pos = -1
    mod = 10**5
    for i in range(K):
        z = (x + sum(map(int, list(str(x)))))%mod
        if z in s:
            break_pos = i
            cycle_start_pos = l.index(z)
            break
        l.append(z)
        s.add(z)
        x = z
    if break_pos == -1:
        print(l[-1])
    else:
        print(l[cycle_start_pos + (K - cycle_start_pos - 1)%(break_pos-cycle_start_pos)])

if __name__ == '__main__':
    main()