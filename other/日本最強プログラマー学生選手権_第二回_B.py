import sys

input = sys.stdin.readline

def main():
    ans = []
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    a = set(A)
    B = list(map(int, input().split()))
    b = set(B)
    for i in range(N):
        if A[i] not in b:
            ans.append(A[i])
    for j in range(M):
        if B[j] not in a:
            ans.append(B[j])
    ans.sort()
    ans = map(str, ans)
    print(' '.join(ans))

if __name__ == '__main__':
    main()