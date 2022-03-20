import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    ans = min(C, B//A)
    print(ans)

if __name__ == '__main__':
    main()