import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C, D, E, F, X = map(int, input().split())
    x = X
    t = 0
    a = 0
    while x > 0:
        t += min(x, A)*B
        x -= A
        x -= C
    x = X
    while x > 0:
        a += min(x, D)*E
        x -= D
        x -= F
    if t > a:
        ans = 'Takahashi'
    elif t < a:
        ans = 'Aoki'
    else:
        ans = 'Draw'

    print(ans)

if __name__ == '__main__':
    main()