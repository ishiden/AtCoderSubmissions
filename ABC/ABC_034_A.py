import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Better'
    x, y = map(int, input().split())
    if x > y:
        ans = 'Worse'

    print(ans)

if __name__ == '__main__':
    main()