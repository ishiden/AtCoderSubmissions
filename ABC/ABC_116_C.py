import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    H = list(map(int, input().split()))
    i = 0
    l = 0
    while i < N - 1:
        while i + 1 < N and H[i] == H[i+1]:
            i += 1
        while i + 1 < N and H[i] <= H[i+1]:
            i += 1
        ans += H[i] - l
        while i + 1 < N and H[i] >= H[i+1]:
            i += 1
        l = H[i]
    if N == 1:
        ans = H[0]
    print(ans)
if __name__ == '__main__':
    main()