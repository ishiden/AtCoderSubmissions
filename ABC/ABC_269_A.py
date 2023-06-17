import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c, d = map(int, input().split())
    print((a+b)*(c-d))
    print('Takahashi')

if __name__ == '__main__':
    main()