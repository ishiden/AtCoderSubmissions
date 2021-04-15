import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, M, T = map(int, input().split())
    maxN = N
    B, c = 0, 0
    for i in range(M):
        A, B = map(int, input().split())
        N -= A - c
        if N <= 0:
            ans = 'No'
            break
        N = min(N + (B - A), maxN)
        c = B
    if N - (T - B) <= 0:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()