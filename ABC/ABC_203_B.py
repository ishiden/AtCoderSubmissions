import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += 100 * i + j
    print(ans)

if __name__ == '__main__':
    main()