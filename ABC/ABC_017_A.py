import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    for _ in range(3):
        s, e = map(int, input().split())
        ans += s * e / 10

    print(int(ans))

if __name__ == '__main__':
    main()