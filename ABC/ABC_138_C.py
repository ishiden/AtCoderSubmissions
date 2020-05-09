import sys

input = sys.stdin.readline

def main():
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()
    ans = (m[0] + m[1]) / 2
    for i in range(2,n):
        ans = (ans + m[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()