import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        ans = H * W
    else:
        ans = ((H+1)//2) * ((W+1)//2)
    print(ans)

if __name__ == '__main__':
    main()