import sys

input = sys.stdin.readline

def main():
    ans = 0
    K, A, B = map(int, input().split())
    if B - A <= 2:
        ans = K + 1
    else:
        n = (K - A + 1)
        ans = max(K+1, (B-A)*(n//2) + n%2 + A)
    print(ans)

if __name__ == '__main__':
    main()