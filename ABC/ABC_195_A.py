import sys

input = sys.stdin.readline

def main():
    ans = 0
    M, H = map(int, input().split())
    print('Yes' if H%M == 0 else 'No')

if __name__ == '__main__':
    main()