import sys

input = sys.stdin.readline

def main():
    ans = 0
    X,Y = map(int, input().split())
    while X<=Y:
        ans += 1
        X *= 2
    print(ans)

if __name__ == '__main__':
    main()