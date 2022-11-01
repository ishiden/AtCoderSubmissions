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
    for i in range(2**N):
        x, y = 0, 0
        for j in range(N):
            if 1 << j & i:
                x += V[j]
                y += C[j]
        ans = max(ans, x - y)

    print(ans)

if __name__ == '__main__':
    main()