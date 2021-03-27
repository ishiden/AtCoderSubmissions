import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = [0, list(map(int, input().split())), 0]
    fee_all = A[0]
    for i in range(1, N + 1):
        fee_all += abs(A[i] - A[i - 1])
    print(fee_all)
    for i in range(1, N + 1):
        ans = fee_all - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1] + abs(A[i - 1] - A[i + 1]))
        print(ans)

if __name__ == '__main__':
    main()