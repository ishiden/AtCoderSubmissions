import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B, C, D = -1, -1, -1, -1
    S = [input().rstrip('\n') for _ in range(10)]
    for i in range(10):
        if '#' in S[i] and A == -1:
            A = i + 1
        elif '#' not in S[i] and A != -1:
            B = i
            break

    for i in range(10):
        if S[A-1][i] == '#' and C == -1:
            C = i + 1
            if C == 10:
                D = 10
                break
        elif S[A-1][i] == '.' and C != -1:
            D = i
            break


    if B == -1:
        B = 10
    if D == -1:
        D = 10

    print(A, B)
    print(C, D)


if __name__ == '__main__':
    main()