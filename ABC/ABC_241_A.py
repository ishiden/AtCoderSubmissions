import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A = list(map(int, input().split()))
    ans = A[0]
    for i in range(2):
        ans = A[ans]

    print(ans)

if __name__ == '__main__':
    main()