import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    X, A = map(int, input().split())
    if X >= A:
        ans = 10
    print(ans)

if __name__ == '__main__':
    main()