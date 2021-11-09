import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    Sx, Sy, Gx, Gy = map(int, input().split())
    ans = (Sx * Gy + Gx * Sy)/(Sy+Gy)
    print(ans)

if __name__ == '__main__':
    main()