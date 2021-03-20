import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    x, y = map(int, input().split())
    if abs(x-y) > 2:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()