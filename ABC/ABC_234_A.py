import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def f(T):
    return int(T**2 + 2*T + 3)

def main():
    ans = 0
    t = int(input())
    ans = f(f(f(t) + t) + f(f(t)))
    print(ans)

if __name__ == '__main__':
    main()