import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 4
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if C == W or C == 1:
        ans -= 1
    if R == H or R == 1:
        ans -= 1
    if H == 1:
        ans -= 1
    if W == 1:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()