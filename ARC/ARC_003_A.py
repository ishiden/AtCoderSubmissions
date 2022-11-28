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
    r = input().rstrip('\n')
    d = dict({'A':4, 'B':3, 'C':2, 'D':1, 'F':0})
    for s in r:
        ans += d[s]
    ans /= N
    print(ans)

if __name__ == '__main__':
    main()