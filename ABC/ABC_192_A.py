import sys

input = sys.stdin.readline

def main():
    ans = 0
    X = int(input())
    ans = 100 - X % 100
    print(ans)

if __name__ == '__main__':
    main()