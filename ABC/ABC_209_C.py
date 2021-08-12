import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 1
    mod = 10 ** 9 + 7
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    for i in range(N):
        ans = ans * max(0, C[i] - i) % mod

    print(ans)

if __name__ == '__main__':
    main()