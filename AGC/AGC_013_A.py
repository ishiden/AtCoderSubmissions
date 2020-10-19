import sys

input = sys.stdin.readline

def main():
    ans = 1
    N = int(input())
    A = list(map(int, input().split()))
    # 0:flat, 1:<, 2:>
    f = 0
    for i in range(N-1):
        if A[i] < A[i+1]:
            if f == 2:
                ans += 1
                f = 0
            else:
                f = 1
        elif A[i] > A[i+1]:
            if f == 1:
                ans += 1
                f = 0
            else:
                f = 2
    print(ans)

if __name__ == '__main__':
    main()