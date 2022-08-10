import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = A * B // math.gcd(A, B)
    if ans > 10 ** 18:
        ans = 'Large'
    print(ans)

if __name__ == '__main__':
    main()