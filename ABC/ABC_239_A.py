import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H = int(input())
    ans = (H * (12800000 + H)) ** 0.5
    print(ans)

if __name__ == '__main__':
    main()