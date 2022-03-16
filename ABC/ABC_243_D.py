import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, X = map(int, input().split())
    S = input().rstrip('\n')
    T = []
    for c in S:
        if c == 'U' and len(T) > 0 and T[-1] != 'U':
            T.pop()
        else:
            T.append(c)

    for c in T:
        if c == 'U':
            X //= 2
        elif c == 'L':
            X *= 2
        else:
            X = X*2 + 1
    print(X)

if __name__ == '__main__':
    main()