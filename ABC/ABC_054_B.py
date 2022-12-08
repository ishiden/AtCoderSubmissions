import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, M = map(int, input().split())
    A = [input().rstrip('\n') for _ in range(N)]
    B = [input().rstrip('\n') for _ in range(M)]
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            f = 0
            for k in range(M):
                if A[i+k][j:j+M] != B[k]:
                    f = 1
                    break
            if not f:
                print(ans)
                exit()

    print('No')

if __name__ == '__main__':
    main()
