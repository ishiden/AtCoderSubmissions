import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[1]:
        ans = l[2]
    else:
        ans = l[0]
    print(ans)

if __name__ == '__main__':
    main()