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
    A = list(map(int, input().split()))
    ans = max(A) - min(A)
    print(ans)

if __name__ == '__main__':
    main()