import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, A, X, Y = map(int, input().split())
    ans = max((N - A), 0) * Y + min(N, A) * X
    print(ans)

if __name__ == '__main__':
    main()