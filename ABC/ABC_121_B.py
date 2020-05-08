import sys

input = sys.stdin.readline

def main():
    ans = 0
    n,m,c = map(int, input().split())
    b = list(map(int, input().split()))
    for _ in range(n):
        temp = c
        a = list(map(int, input().split()))
        for j in range(m):
            temp += a[j]*b[j]
        if temp > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
