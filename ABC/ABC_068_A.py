import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = input().rstrip('\n')
    ans = 'ABC' + N.zfill(3)
    print(ans)

if __name__ == '__main__':
    main()