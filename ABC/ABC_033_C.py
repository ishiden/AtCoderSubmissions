import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = list(input().split('+'))
    for s in S:
        if len(s) == 1 and s != '0':
            ans += 1
        else:
            if '0' not in s:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()