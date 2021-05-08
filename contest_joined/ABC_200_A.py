import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    ans = N//100
    if N % 100 != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()