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
    ans = s[0] + str(len(s)-2) + s[-1]
    print(ans)

if __name__ == '__main__':
    main()