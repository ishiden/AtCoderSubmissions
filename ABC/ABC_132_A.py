import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    S = input().rstrip('\n')
    c = collections.Counter(S)
    if len(c) == 2 and c[0] == c[1]:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()