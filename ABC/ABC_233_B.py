import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    L, R = map(int, input().split())
    S = input().rstrip('\n')
    ans = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(ans)

if __name__ == '__main__':
    main()