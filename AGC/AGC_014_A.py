import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c = map(int, input().split())
    while a%2 == b%2 == c%2 == 0:
        ans += 1
        a, b, c = (b//2 + c//2), (a//2 + c//2), (a//2 + b//2)
        if a == b == c:
            ans = -1
            break
    print(ans)

if __name__ == '__main__':
    main()