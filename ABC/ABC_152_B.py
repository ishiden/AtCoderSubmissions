import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    a, b = input().split()
    A = a * int(b)
    B = b * int(a)
    ans = [A, B]
    ans.sort()
    print(ans[0])

if __name__ == '__main__':
    main()