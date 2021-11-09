import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = -1
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i%C == 0:
            ans = i
            break

    print(ans)

if __name__ == '__main__':
    main()