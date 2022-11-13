import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A = int(input())
    if A%2 == 0:
        ans = (A//2)**2
    # else:
    #     ans = (A//2) * (A//2+1)
    print(ans)

if __name__ == '__main__':
    main()