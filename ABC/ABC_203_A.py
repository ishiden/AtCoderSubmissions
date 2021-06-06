import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c = map(int, input().split())
    if a == b:
        ans = c
    elif a == c:
        ans = b
    elif b == c:
        ans = a
    print(ans)

if __name__ == '__main__':
    main()