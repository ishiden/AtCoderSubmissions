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
    l = []
    for i in range(N):
        s = ''.join(sorted(list(input().rstrip('\n'))))
        l.append(s)
    l.sort()
    c = 1
    for i in range(N):
        if i < N - 1 and l[i] == l[i+1]:
            c += 1
        else:
            if c >= 2:
                ans += c * (c - 1) // 2
            c = 1

    print(ans)

if __name__ == '__main__':
    main()