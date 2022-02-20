import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i-1] == A[i] - 1:
            ans += C[A[i]-2]

    print(ans)

if __name__ == '__main__':
    main()