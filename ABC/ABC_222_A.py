import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = input().rstrip('\n')
    ans = '0'* (4-len(N)) + N
    print(ans)

if __name__ == '__main__':
    main()