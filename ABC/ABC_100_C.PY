import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N):
        if a[i]%2 == 0:
            while a[i]%2 == 0:
                a[i] = a[i]//2
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()