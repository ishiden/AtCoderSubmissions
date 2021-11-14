import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    N, K, A = map(int, input().split())
    pos = A
    K -= 1
    while K > 0:
        if pos + 1 > N:
            pos = 1
        else:
            pos += 1
        K -= 1

    print(pos)

if __name__ == '__main__':
    main()