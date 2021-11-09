import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = ['ABC', 'ARC', 'AGC', 'AHC']
    for _ in range(3):
        ans.remove(input().rstrip('\n'))

    print(*ans)

if __name__ == '__main__':
    main()