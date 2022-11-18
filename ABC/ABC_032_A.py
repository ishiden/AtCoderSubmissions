import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    a = int(input())
    b = int(input())
    n = int(input())
    lcm = a * b / math.gcd(a, b)
    if lcm < n:
        lcm *= math.ceil(n/lcm)
    print(int(lcm))

if __name__ == '__main__':
    main()