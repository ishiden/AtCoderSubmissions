import sys

input = sys.stdin.readline

def main():
    ans = 2 ** 30 + 1
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(2 ** N - 1):
        or_ = 0
        xor_ = 0
        for j in range(N + 1):
            if j < N:
                or_ |= A[j]
            if j == N or i >> j & 1:
                xor_ ^= or_
                or_ = 0
        ans = min(ans, xor_)

    print(ans)

if __name__ == '__main__':
    main()