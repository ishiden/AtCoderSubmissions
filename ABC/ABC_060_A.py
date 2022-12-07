import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    A, B, C = input().split()
    if A[-1] == B[0] and B[-1] == C[0]:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()