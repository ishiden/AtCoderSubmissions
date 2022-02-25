import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    setA = set(A)
    print(len(setA))

if __name__ == '__main__':
    main()