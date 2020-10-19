import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, A, B = map(int, input().split())
    ans = N - A + B
    print(ans)

if __name__ == '__main__':
    main()