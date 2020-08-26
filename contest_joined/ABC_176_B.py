import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    n = int(input())
    if n%9 != 0:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()