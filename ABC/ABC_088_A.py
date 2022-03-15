import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    A = int(input())
    N %= 500
    if N > A:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()