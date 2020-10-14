import sys

input = sys.stdin.readline

def main():
    ans = 'YES'
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))
    if N < M:
        ans = 'NO'
    else:
        D.sort()
        T.sort()
        at = 0
        for i in range(M):
            while T[i] > D[at]:
                at += 1
            if T[i] != D[at]:
                ans = 'NO'
                break
            at += 1
    print(ans)

if __name__ == '__main__':
    main()