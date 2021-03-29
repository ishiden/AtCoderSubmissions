import sys

input = sys.stdin.readline

def main():
    ans = 10**9 + 1
    n = int(input())
    for _ in range(n):
        A, P, X = map(int, input().split())
        ans = min(ans, P if X - A > 0 else ans)
    print(-1 if ans == 10**9 + 1 else ans)

if __name__ == '__main__':
    main()