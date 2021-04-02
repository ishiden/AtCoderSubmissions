import sys

input = sys.stdin.readline

def main():
    ans = 'Takahashi'
    A, B, C = map(int, input().split())
    if C == 0:
        A -= 1
    if A < B:
        ans = 'Aoki'
    print(ans)

if __name__ == '__main__':
    main()