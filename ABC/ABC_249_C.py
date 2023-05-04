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
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input().rstrip('\n'))
    for i in range(2**N):
        counter = collections.defaultdict(int)
        tmp = 0
        for j in range(N):
            if (i >> j) & 1:
                for s in S[j]:
                    counter[s] += 1
        for val in counter.values():
            if val == K:
                tmp += 1
        if ans < tmp:
            ans = tmp

    print(ans)

if __name__ == '__main__':
    main()