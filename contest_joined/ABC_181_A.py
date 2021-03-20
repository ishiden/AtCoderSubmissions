import sys

input = sys.stdin.readline

def main():
    ans = 'Black'
    N = int(input())
    if N%2 == 0:
        ans = 'White'
    print(ans)

if __name__ == '__main__':
    main()