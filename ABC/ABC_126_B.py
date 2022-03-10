import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NA'
    S = input().rstrip('\n')
    fh = int(S[:2])
    lh = int(S[2:])
    if 1 <= fh <= 12 and 1 <= lh <= 12:
        ans = 'AMBIGUOUS'
    elif 1 <= fh <= 12:
        ans = 'MMYY'
    elif 1 <= lh <= 12:
        ans = 'YYMM'

    print(ans)

if __name__ == '__main__':
    main()