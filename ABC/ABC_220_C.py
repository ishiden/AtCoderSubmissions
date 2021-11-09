import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    Asum = sum(A)
    if X > Asum:
        ans += X//Asum * N
        X %= Asum
    temp = 0
    for i in range(N):
        temp += A[i]
        ans += 1
        if temp > X:
            break

    print(ans)

if __name__ == '__main__':
    main()