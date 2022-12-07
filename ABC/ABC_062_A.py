import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    x, y = map(int, input().split())
    s1 = set([1, 3, 5, 7, 8, 10, 12])
    s2 = set([4, 6, 9, 11])
    if x != 2 and y != 2:
        if (x in s1 and y in s1) or (x in s2 and y in s2):
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()