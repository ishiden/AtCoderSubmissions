import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = [False] * N

    for a in range(1, 200):
        for b in range(1, 200):
            temp = 3 * (a + b) + 4 * a * b
            T = [i for i, x in enumerate(S) if x == temp]
            for t in T:
                ans[t] = True

    print(ans.count(False))

if __name__ == '__main__':
    main()