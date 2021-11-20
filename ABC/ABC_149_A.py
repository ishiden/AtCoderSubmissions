import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = ''
    S, T = input().split()
    ans = T + S
    print(ans)

if __name__ == '__main__':
    main()