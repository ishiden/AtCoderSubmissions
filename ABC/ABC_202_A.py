import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c = map(int, input().split())
    ans = 21 - (a + b + c)
    print(ans)

if __name__ == '__main__':
    main()