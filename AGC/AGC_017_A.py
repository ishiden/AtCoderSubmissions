import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    odd = 0
    for i in range(N):
        if A[i] % 2 != 0:
            odd += 1
    ans = 2 ** (N - 1)
    if odd == 0:
        ans = 0 if P == 1 else 2 ** N
    print(ans)

if __name__ == '__main__':
    main()