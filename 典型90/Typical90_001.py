import sys
import collections
import heapq

input = sys.stdin.readline

def check(A, N, L, K, X):
    num = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= X:
            num += 1
            pre = A[i]
    if L - pre >= X:
        num += 1
    return num >= K + 1


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    l = 0
    r = L
    while r - l > 1:
        mid = (r + l) // 2
        if check(A, N, L, K, mid):
            l = mid
        else:
            r = mid

    print(l)

if __name__ == '__main__':
    main()