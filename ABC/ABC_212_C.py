import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 10**9 + 1
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ap = bp = 0
    while ap < N and bp < M:
        ans = min(ans, abs(A[ap] - B[bp]))
        if A[ap] < B[bp]:
            ap += 1
        elif A[ap] > B[bp]:
            bp += 1
        else:
            break

    print(ans)

if __name__ == '__main__':
    main()