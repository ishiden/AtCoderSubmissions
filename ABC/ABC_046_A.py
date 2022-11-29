import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c = map(int, input().split())
    ans = len(set([a, b, c]))
    print(ans)

if __name__ == '__main__':
    main()