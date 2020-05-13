import sys

input = sys.stdin.readline

def main():
    ans = float('inf')
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        tmp = 0
        while a[i]%2 == 0:
            a[i] //= 2
            tmp += 1
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()