import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = '4:3'
    W, H = map(int, input().split())
    if W/16 == H/9:
        ans = '16:9'

    print(ans)

if __name__ == '__main__':
    main()