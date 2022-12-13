import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    mod = 10**9+7
    L, R = map(int, input().split())
    for i in range(1, 20):
        if L <= 10**(i-1) and (10**i)-1 <= R:
            a, b = 10**(i-1), (10**i)-1
        elif 10**(i-1) <= L and R < 10**i:
            a, b = L, R
        elif 10**(i-1) <= L < 10**i:
            a, b = L, (10**i)-1
        elif 10**(i-1) <= R < 10**i:
            a, b = 10**(i-1), R
        else:
            continue
        sub = (a+b) * (b-a+1) // 2
        ans += sub * i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()