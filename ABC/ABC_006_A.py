import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    n = int(input())
    if n % 3 == 0 or '3' in str(n):
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()