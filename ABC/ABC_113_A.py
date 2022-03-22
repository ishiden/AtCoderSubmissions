import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    X, Y = map(int, input().split())
    ans = X + Y//2
    print(ans)

if __name__ == '__main__':
    main()