import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    H = list(map(int, input().split()))
    m = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            m += 1
        else:
            m = 0
        ans = max(ans, m)
    print(ans)

if __name__ == '__main__':
    main()