import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans_a = 0
    ans_b = 0
    N = int(input())
    A = list(map(int, input().split()))
    avg_A = math.ceil(sum(A)/N)
    avg_B = math.floor(sum(A)/N)
    for a in A:
        ans_a += (a - avg_A)**2
        ans_b += (a - avg_B)**2
    print(min(ans_a, ans_b))

if __name__ == '__main__':
    main()