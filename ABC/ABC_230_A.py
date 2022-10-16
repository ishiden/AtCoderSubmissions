import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    if N > 41:
        N += 1
    ans = 'AGC' + str(N).zfill(3)
    print(ans)

if __name__ == '__main__':
    main()