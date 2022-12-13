import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0] + a[1]

    print(ans)

if __name__ == '__main__':
    main()