import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if (i+1)%2==1 and a[i]%2==1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()