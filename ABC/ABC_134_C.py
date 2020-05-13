import sys

input = sys.stdin.readline

def main():
    ans = ''
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    M, M2 = sorted(A)[-1], sorted(A)[-2]
    for i in range(N):
        if A[i] == M:
          ans += str(M2) + '\n'
        else:
          ans += str(M) + '\n'
    print(ans)

if __name__ == '__main__':
    main()