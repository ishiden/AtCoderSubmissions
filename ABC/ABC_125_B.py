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
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]

    print(ans)

if __name__ == '__main__':
    main()