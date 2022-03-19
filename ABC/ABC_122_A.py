import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    e = 'ACGT'
    t = 'TGCA'
    b = input().rstrip('\n')
    ans = t[e.index(b)]
    print(ans)

if __name__ == '__main__':
    main()