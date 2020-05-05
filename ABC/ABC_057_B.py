import sys

input = sys.stdin.readline

# def main():
#     n,m = map(int, input().split())
#     a = [0]*n
#     b = [0]*n
#     c = [0]*m
#     d = [0]*m
#     ans = [1]*n
#     for i in range(n):
#         a[i], b[i] = map(int, input().split())
#     for i in range(m):
#         c[i], d[i] = map(int, input().split())
#     for i in range(n):
#         temp = abs(a[i]-c[0]) + abs(b[i]-d[0])
#         for j in range(1,m):
#             cur = abs(a[i]-c[j]) + abs(b[i]-d[j])
#             if temp > cur:
#                 temp = cur
#                 ans[i] = j+1
#         print(ans[i])

# if __name__ == '__main__':
#     main()

def main():
    n,m = map(int, input().split())
    s = []
    p = []
    min = [10**12]*n
    ans = [0]*n
    for _ in range(n):
        s.append(list(map(int, input().split())))
    for _ in range(m):
        p.append(list(map(int, input().split())))
    for i in range(n):
        a, b = s[i]
        for j in range(m):
            c,d  = p[j]
            md = abs(a-c) + abs(b-d)
            if md < min[i]:
                min[i] = md
                ans[i] = j+1
        print(ans[i])

if __name__ == '__main__':
    main()