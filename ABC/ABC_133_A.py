import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, A, B = map(int, input().split())
    ans = min(N*A, B)
    print(ans)

if __name__ == '__main__':
    main()