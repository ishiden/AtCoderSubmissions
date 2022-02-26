import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = []
    c = 0
    for i in range(N):
        if len(l) == 0 or l[-1][0] != A[i]:
            l.append([A[i], 1])
            c += 1
        elif l[-1][0] == A[i]:
            if l[-1][1] + 1 == A[i]:
                t = l.pop()
                c -= t[1]
            else:
                l[-1][1] += 1
                c += 1
        print(c)

if __name__ == '__main__':
    main()