import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for i in range(1,n):
        if a[i-1] > a[i]:
            tmp = a[i-1]-a[i]
            ans += tmp
            a[i] += tmp
    print(ans)

if __name__ == '__main__':
    main()