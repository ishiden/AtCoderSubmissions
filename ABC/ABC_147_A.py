import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'win'
    if sum(map(int, input().split())) >= 22:
        ans = 'bust'
    print(ans)

if __name__ == '__main__':
    main()