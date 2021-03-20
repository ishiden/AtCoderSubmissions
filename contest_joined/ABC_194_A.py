import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    if A + B >= 15 and B >= 8:
        ans = "1"
    elif A + B >= 10 and B >= 3:
        ans = "2"
    elif A + B >= 3:
        ans = "3"
    else:
        ans = "4"
    print(ans)

if __name__ == '__main__':
    main()