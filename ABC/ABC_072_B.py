import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = ''
    s = input().rstrip('\n')
    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]

    print(ans)

if __name__ == '__main__':
    main()