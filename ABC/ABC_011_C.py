import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'YES'
    N = int(input())
    NG = []
    for _ in range(3):
        NG.append(int(input()))
    cnt = 0
    if N not in NG:
        while N > 0:
            if N - 3 not in NG:
                N -= 3
            elif N - 2 not in NG:
                N -= 2
            elif N - 1 not in NG:
                N -= 1
            else:
                ans = 'NO'
                break
            cnt += 1
    if N in NG or cnt > 100:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()