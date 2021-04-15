import sys

input = sys.stdin.readline

def main():
    ans = 0
    R, X, Y = map(int, input().split())
    X *= X
    Y *= Y
    d = X + Y
    ans = d**0.5 // R
    if d**0.5 % R != 0:
        ans += 1
    if d**0.5 < R:
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()