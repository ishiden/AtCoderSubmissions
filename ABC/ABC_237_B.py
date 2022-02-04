import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    A = [] * W
    for i in range(H):
        a = list(input().split())
        A.append(a)

    for i in range(W):
        for j in range(H):
            if j != 0:
                print(' ', end="")
            print(A[j][i], end="")
        print()



if __name__ == '__main__':
    main()