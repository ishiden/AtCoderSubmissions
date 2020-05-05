import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b, x = map(int, input().split())
    a -= 1
    la = a//x
    lb = b//x
    ans = lb - la
    print(ans)

if __name__ == '__main__':
    main()