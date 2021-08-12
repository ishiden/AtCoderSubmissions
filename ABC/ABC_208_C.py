import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    eq, ex = 0, 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sorted_A = sorted(A)
    if K >= N:
        eq = K // N
    ex = K % N
    h = {}
    for i, a in enumerate(sorted_A):
        if i <= ex - 1:
            h[a] = True
        else:
            h[a] = False

    for a in A:
        if h[a]:
            print(eq + 1)
        else:
            print(eq)

if __name__ == '__main__':
    main()