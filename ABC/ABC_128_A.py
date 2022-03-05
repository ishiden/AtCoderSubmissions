import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, P = map(int, input().split())
    P += A * 3
    ans = P//2
    print(ans)

if __name__ == '__main__':
    main()