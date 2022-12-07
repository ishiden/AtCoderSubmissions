import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    A, B, C = map(int, input().split())
    if A <= C <= B:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()