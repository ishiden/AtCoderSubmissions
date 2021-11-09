import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'Yes'
    X = int(input())
    if X == 0:
        ans = 'No'
    elif X % 100 != 0:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()