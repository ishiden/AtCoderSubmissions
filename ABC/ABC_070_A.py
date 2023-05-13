import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'No'
    N = list(input().rstrip('\n'))
    if N[0] == N[-1]:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()