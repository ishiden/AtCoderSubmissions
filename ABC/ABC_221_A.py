import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = (B-A)*32
    print(ans)

if __name__ == '__main__':
    main()