import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    a, b, c = map(int, input().split())
    if a < c**b:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()