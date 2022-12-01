import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B, C, D = map(int, input().split())
    ans = max(A*B, C*D)
    print(ans)

if __name__ == '__main__':
    main()