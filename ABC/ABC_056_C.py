import sys

input = sys.stdin.readline

def main():
    ans, d = 0, 0
    X = int(input())
    for i in range(1, X + 1):
        if d >= X:
            break
        d += i
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()