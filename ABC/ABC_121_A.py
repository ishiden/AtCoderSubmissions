import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    ans = (H - h) * (W - w)
    print(ans)

if __name__ == '__main__':
    main()