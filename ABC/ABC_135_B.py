import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'YES'
    N = int(input())
    P = list(map(int, input().split()))
    v = 0
    c = 0
    for i in range(1, N+1):
        if P[i-1] != i:
            if v != 0:
                if v != i or c == 1:
                    ans = 'NO'
                    break
                else:
                    c = 1
            else:
                v = P[i-1]
    print(ans)

if __name__ == '__main__':
    main()