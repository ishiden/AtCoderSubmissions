import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    l = list(map(int, input().split()))
    inf = 10**9
    dp = [inf] * (N + 1)
    dp[0] = 0
    for i in range(0, N - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(l[i] - l[i + 1]))
        if i < N - 2:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(l[i] - l[i + 2]))

    print(dp[N - 1])

if __name__ == '__main__':
    main()