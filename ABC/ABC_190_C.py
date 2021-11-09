import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N, M = map(int, input().split())
    cond = []
    for i in range(M):
        A, B = map(int, input().split())
        cond.append([A, B])

    K = int(input())
    choice = []
    for i in range(K):
        C, D = map(int, input().split())
        choice.append([C, D])

    for balls in itertools.product(*choice):
        balls = set(balls)
        cnt = sum(A in balls and B in balls for A, B in cond)
        ans = max(ans, cnt)

    print(ans)

if __name__ == '__main__':
    main()