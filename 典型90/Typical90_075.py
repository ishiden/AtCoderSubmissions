import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    ans = 0
    N = int(input())
    x = prime_factorize(N)
    c = 1
    while c < len(x):
        ans += 1
        c *= 2

    print(ans)

if __name__ == '__main__':
    main()