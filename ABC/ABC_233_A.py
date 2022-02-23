import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    X, Y = map(int, input().split())
    ans = ((Y + 9) - X)//10

    print(max(ans, 0))

if __name__ == '__main__':
    main()