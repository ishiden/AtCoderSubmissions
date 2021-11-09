import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    K = int(input())
    A, B = map(list, input().split())
    tA, tB = 0, 0
    for i in range(len(A)):
        tA += K**i*int(A[-(i+1)])
    for i in range(len(B)):
        tB += K**i*int(B[-(i+1)])
    ans = tA*tB

    print(ans)

if __name__ == '__main__':
    main()