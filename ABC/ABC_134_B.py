import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, D = map(int, input().split())
    ans = math.ceil(N / (2 * D + 1))
    print(ans)

if __name__ == '__main__':
    main()