import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    c = C // A
    ans = c + (C - c*A)//B

    print(ans)

if __name__ == '__main__':
    main()