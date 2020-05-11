import sys

input = sys.stdin.readline

def main():
    ans = float('INF')
    n, m, x = map(int, input().split())
    c = [0]*n
    a = [[]for _ in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        c[i], a[i] = temp[0], temp[1:]
    for bit in range(1<<n):
        acquired = True
        cost = 0
        d = [0]*m
        for i in range(n):
            if (bit&(1 << i)):
                cost += c[i]
                for j in range(m):
                    d[j] += a[i][j]
        for k in range(m):
            if d[k] < x:
                acquired = False
        if acquired:
            ans = min(ans, cost)
    if ans == float('INF'):
        ans = -1

    print(ans)

if __name__ == '__main__':
    main()

# コンテスト中に解けず
# import sys

# input = sys.stdin.readline

# def main():
#     ans = 0
#     n, m, x = map(int, input().split())
#     sum = [x]*m
#     a = []
#     for i in range(n):
#         a.append(list(map(int, input().split())))
#     for i in range(n):
#         for j in range(1,m):
#             sum[j] += a[j]

#     print(ans)

# if __name__ == '__main__':
#     main()