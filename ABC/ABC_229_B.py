import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'Easy'
    A, B = input().split()
    minDigi = min(len(A), len(B))
    for i in range(1, minDigi+1):
        if int(A[-i]) + int(B[-i]) > 9:
            ans = 'Hard'
            break
    print(ans)

if __name__ == '__main__':
    main()