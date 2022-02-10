import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    t = 0
    for i in range(N):
        if S[i] == T[t]:
            print('Yes')
            t += 1
        else:
            print('No')

if __name__ == '__main__':
    main()