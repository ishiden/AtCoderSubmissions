import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    ans = N * (N - 1) // 2
    C = collections.Counter(A)
    for i in C.values():
        if i > 1:
            ans -= i * (i - 1) // 2

    print(ans)

if __name__ == '__main__':
    main()