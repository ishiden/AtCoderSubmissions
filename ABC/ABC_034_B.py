import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    if n%2 == 0:
        ans = n - 1
    else:
        ans = n + 1
    print(ans)

if __name__ == '__main__':
    main()