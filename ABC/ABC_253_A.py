import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'No'
    a, b, c = map(int, input().split())
    l = [a, b, c]
    l.sort()
    if l[1] == b:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()