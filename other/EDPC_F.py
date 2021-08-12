import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    dp = [[0] * (len_s + 1) for i in range(len_t + 1)]
    for i in range(len_s - 1):
        for j in range(len_t - 1):
            if i > 0 and j > 0:
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    _len = dp[len_s - 1][len_t - 1]
    i = len_s
    j = len_t
    while _len > 0:
        if s[i] == t[j]:
            ans += s[i]
            i -= 1
            j -= 1
            _len -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    print(ans)

if __name__ == '__main__':
    main()