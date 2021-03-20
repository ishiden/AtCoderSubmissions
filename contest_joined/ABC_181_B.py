import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        ans += (A+B)*(B - A + 1)/2
    print(ans)

if __name__ == '__main__':
    main()