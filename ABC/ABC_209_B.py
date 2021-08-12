import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 != 0:
            X -= (A[i] - 1)
        else:
            X -= A[i]
        if X < 0:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()