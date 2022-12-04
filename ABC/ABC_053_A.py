import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'ABC'
    x = int(input())
    if x >= 1200:
        ans = 'ARC'

    print(ans)

if __name__ == '__main__':
    main()