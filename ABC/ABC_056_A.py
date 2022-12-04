import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    a, b = input().split()
    if a == 'H':
        if b == 'H':
            ans = 'H'
        else:
            ans = 'D'
    else:
        if b == 'H':
            ans = 'D'
        else:
            ans = 'H'
    print(ans)

if __name__ == '__main__':
    main()