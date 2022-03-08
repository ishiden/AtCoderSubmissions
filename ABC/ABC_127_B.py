import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    r, D, x = map(int, input().split())
    for i in range(10):
        ans = r * x - D
        x = ans
        print(ans)

if __name__ == '__main__':
    main()