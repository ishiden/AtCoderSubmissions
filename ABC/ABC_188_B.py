import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ip = 0
    for i in range(n):
        ip += A[i] * B[i]
    if ip != 0:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()