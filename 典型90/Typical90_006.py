import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    S = input().rstrip('\n')
    ans = ''
    start = 0
    end = N - K + 1
    for i in range(K):
        s = min(S[start:end])
        start = start + S[start:end].index(s) + 1
        end += 1
        ans += s

    print(ans)

if __name__ == '__main__':
    main()