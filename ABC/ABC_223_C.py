import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = []
    B = []
    now = 0
    timels = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        timels.append(a/b)
    r = sum(timels) / 2
    for i in range(N):
        now += timels[i]
        if now == r:
            ans = sum(A[:i+1])
            break
        elif now > r:
            ans = sum(A[:i+1]) - (now-r)*B[i]
            break

    print(ans)

if __name__ == '__main__':
    main()