import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    ans = A * B / math.gcd(A, B)

    print(int(ans))

if __name__ == '__main__':
    main()