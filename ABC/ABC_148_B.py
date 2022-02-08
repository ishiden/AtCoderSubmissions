import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], end='', sep='')
    print()

if __name__ == '__main__':
    main()