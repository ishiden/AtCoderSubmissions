import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    ans = A * B * 2 + A * C * 2 + B * C * 2
    print(ans)

if __name__ == '__main__':
    main()