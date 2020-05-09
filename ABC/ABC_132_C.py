import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans += d[n//2] - d[n//2-1]
    print(ans)

if __name__ == '__main__':
    main()