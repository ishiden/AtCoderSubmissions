import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    if N >= 1000:
        ans += N - 999
    if N >= 1000000:
        ans += (N - 999999)
    if N >= 1000000000:
        ans += (N - 999999999)
    if N >= 1000000000000:
        ans += (N - 999999999999)
    if N >= 1000000000000000:
        ans += (N - 999999999999999)
    print(ans)

if __name__ == '__main__':
    main()