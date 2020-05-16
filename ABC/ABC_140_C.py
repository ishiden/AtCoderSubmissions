import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    B = list(map(int, input().split()))
    for i in range(N-2):
        ans += min(B[i], B[i+1])
    ans += B[-1] + B[0]
    print(ans)

if __name__ == '__main__':
    main()