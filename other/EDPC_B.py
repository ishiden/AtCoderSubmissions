import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [10**9] * N
    dp[0] = 0
    for i in range(N):
        for k in range(1, K + 1):
            if i + k > N - 1:
                break
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))

    print(dp[N - 1])

if __name__ == '__main__':
    main()