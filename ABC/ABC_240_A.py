import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    a, b = map(int, input().split())
    if b-a == 1 or a == 1 and b == 10:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()