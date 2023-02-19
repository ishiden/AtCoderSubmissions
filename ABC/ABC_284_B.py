import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    T = int(input())
    for _ in range(T):
        ans = 0
        N = int(input())
        A = list(map(int, input().split()))
        for i in range(N):
            if A[i]%2 != 0:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()