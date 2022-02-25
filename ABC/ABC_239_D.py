import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return False
    sn = int(math.sqrt(n))
    for i in range(2, sn + 1):
        if n%i == 0:
            return False
    return True

def main():
    ans = 'Aoki'
    A, B, C, D = map(int, input().split())
    for i in range(A, B+1):
        canPrime = False
        for j in range(C, D+1):
            if isPrime(i + j):
                canPrime = True
        if canPrime == False:
            ans = 'Takahashi'
            break
    print(ans)

if __name__ == '__main__':
    main()