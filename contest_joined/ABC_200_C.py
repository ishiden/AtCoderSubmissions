import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    l = [0]*200
    for i in range(N):
        l[A[i]%200] += 1
    for i in range(200):
        ans += l[i] * (l[i]-1) // 2

    print(ans)

if __name__ == '__main__':
    main()