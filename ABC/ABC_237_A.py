import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    if -2**31 <= N < 2**31:
        ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()