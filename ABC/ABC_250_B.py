import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = ''
    N, A, B = map(int, input().split())
    colors = ['.', '#']
    a, b = 0, 0
    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += colors[b]*B
            b = not b
        tmp += '\n'
        ans += tmp * A
        b = not a
        a = not a

    print(ans)

if __name__ == '__main__':
    main()