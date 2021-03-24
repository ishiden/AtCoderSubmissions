import sys

input = sys.stdin.readline

def main():
    N = int(input())
    H = list(map(int, input().split()))
    dp = []
    dp.append(0)
    for i in range(1, N):
        cost = dp[i-1] + abs(H[i - 1] - H[i])
        if i > 1:
            cost = min(cost, dp[i - 2] + abs(H[i - 2] - H[i]))
        dp.append(cost)
    print(dp[N-1])

if __name__ == '__main__':
    main()