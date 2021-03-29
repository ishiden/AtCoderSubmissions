import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = 100 - (B / A * 100)
    print(ans)

if __name__ == '__main__':
    main()