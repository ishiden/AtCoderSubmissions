import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = -1
    A, B = map(int, input().split())
    if A <= 9 and B <= 9:
        ans = A * B
    print(ans)

if __name__ == '__main__':
    main()