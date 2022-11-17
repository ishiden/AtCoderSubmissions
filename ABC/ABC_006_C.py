import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    for i in range(2):
        for j in range(N-i+1):
            k = N - (i+j)
            if i*3 + j*2 + k*4 == M:
                print(j, i, k)
                exit()
    print(-1, -1, -1)

if __name__ == '__main__':
    main()