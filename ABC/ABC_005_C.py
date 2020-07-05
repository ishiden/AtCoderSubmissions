import sys

input = sys.stdin.readline

def main():
    ans = 'yes'
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    l = [False]*M
    if N >= M:
        s = 0
        for i in range(M):
            while s < N:
                if A[s] <= B[i] <= A[s]+T:
                    s += 1
                    l[i] = True
                    break
                else:
                    s += 1
            if len(A[s:]) < len(B[i+1:]):
                break
    if False in l:
        ans = 'no'
    print(ans)

if __name__ == '__main__':
    main()
