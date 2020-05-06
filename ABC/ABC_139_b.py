import sys

input = sys.stdin.readline

def main():
    ans = 0
    a,b = map(int, input().split())
    while ans * a - (ans - 1) < b:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()