import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

if __name__ == '__main__':
    main()