import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b = map(int, input().split())

    print(100*(a-b)/a)

if __name__ == '__main__':
    main()