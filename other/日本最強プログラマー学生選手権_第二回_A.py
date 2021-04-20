import sys

input = sys.stdin.readline

def main():
    ans = 0
    X, Y, Z = map(int, input().split())
    ans = int(Y / X * Z)
    if ans / Z >= Y / X:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()