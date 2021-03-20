import sys

input = sys.stdin.readline

def main():
    ans = 0
    l = []
    N = int(input())
    dp = []
    for i in range(N+1):
        dp.append([0,0,0])
        if i <= N-1:
            a,b,c = list(map(int, input().split()))
            l.append([a,b,c])
    for i in range(1, N+1):
        dp[i][0] = max(dp[i-1][1] + l[i-1][0], dp[i-1][2] + l[i-1][0])
        dp[i][1] = max(dp[i-1][2] + l[i-1][1], dp[i-1][0] + l[i-1][1])
        dp[i][2] = max(dp[i-1][0] + l[i-1][2], dp[i-1][1] + l[i-1][2])
    print(max(dp[N][0],max(dp[N][1], dp[N][2])))

if __name__ == '__main__':
    main()