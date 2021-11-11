import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    e = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        e[a-1].append(b-1)
        e[b-1].append(a-1)
    for i in range(N):
        if len(e[i]) == N - 1:
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()