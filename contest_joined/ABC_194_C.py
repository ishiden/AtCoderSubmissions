import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    l = [0]*401
    for i in range(N):
        l[A[i] + 200] += 1
    for i in range(400):
        for j in range(1,401):
            ans += l[i] * l[j] * (i - j)**2
    print(ans)

if __name__ == '__main__':
    main()