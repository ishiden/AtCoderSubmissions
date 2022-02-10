import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    K, X = map(int, input().split())
    if 500 * K >= X:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()