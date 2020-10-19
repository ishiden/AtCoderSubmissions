import sys

input = sys.stdin.readline

def main():
    ans = 0
    X, Y, A, B = map(int, input().split())
    while X*A < X+B and X*A < Y:
        X *= A
        ans += 1
    if X + B < Y:
        ans += (Y - X - 1)//B
    print(ans)

if __name__ == '__main__':
    main()