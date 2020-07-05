import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    ans += N//10*100 + min(N%10*15, 100)
    print(ans)

if __name__ == '__main__':
    main()