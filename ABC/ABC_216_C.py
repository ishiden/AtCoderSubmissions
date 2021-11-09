import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = ''
    N = int(input())
    b = int(N ** 0.5)
    while(N > 0):
        if N % 2 != 0:
            ans += 'A'
            N -= 1
        else:
            ans += 'B'
            N //= 2
    print(ans[::-1])

if __name__ == '__main__':
    main()