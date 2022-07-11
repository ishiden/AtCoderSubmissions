import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        ans += abs(a[i] - b[i])
    print(ans)

if __name__ == '__main__':
    main()