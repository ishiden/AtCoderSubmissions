import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    while i < N-1:
        while i+1 < N and A[i] == A[i+1]:
            i += 1
        if i+1 < N and A[i] < A[i+1]:
            while i+1 < N and A[i] <= A[i+1]:
                i += 1
        elif i+1 < N and A[i] > A[i+1]:
            while i+1 < N and A[i] >= A[i+1]:
                i += 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()

# undone 20201006