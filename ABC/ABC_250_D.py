import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def Elatosthenes(n):
    isprime = [True] * (n+1)
    isprime[0], isprime[1] = False, False
    for p in range(2, n+1):
        if not isprime[p]:
            continue
        q = p * 2
        while q <= n:
            isprime[q] = False
            q += p
    primes = []
    for i in range(2, n+1):
        if isprime[i]:
            primes.append(i)
    return primes

def main():
    ans = 0
    N = int(input())
    primes = Elatosthenes(10**6)
    q = len(primes)-1
    for i in range(len(primes)):
        while 0 < q and primes[i]*primes[q]**3 > N:
            q -= 1
        if q <= i:
            break
        ans += q - i

    print(ans)

if __name__ == '__main__':
    main()