import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Draw'
    A, B = map(int, input().split())
    if A == 1:
        A += 13
    if B == 1:
        B += 13
    if A > B:
        ans = 'Alice'
    if A < B:
        ans = 'Bob'
    print(ans)

if __name__ == '__main__':
    main()