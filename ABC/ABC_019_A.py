import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    o = list(map(int, input().split()))
    o.sort()

    print(o[1])

if __name__ == '__main__':
    main()