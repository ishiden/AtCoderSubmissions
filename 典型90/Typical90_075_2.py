import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    max_i = int(N**0.5)
    cnt = 0
    for i in range(2, max_i+1):
        while N % i == 0:
            cnt += 1
            N //= i
    if N != 1:
        cnt += 1

    tmp = 1
    while tmp < cnt:
        tmp *= 2
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()