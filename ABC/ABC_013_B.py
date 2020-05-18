import sys

input = sys.stdin.readline

def main():
    ans = 0
    a = int(input())
    b = int(input())
    ans = abs(a-b)
    if ans > 5:
        ans = 10 - ans
    print(ans)

if __name__ == '__main__':
    main()