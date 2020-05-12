import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    d, x = map(int, input().split())
    a = 0
    for _ in range(n):
        a = int(input())
        ans += 1 + (d-1)//a
    print(ans+x)

if __name__ == '__main__':
    main()