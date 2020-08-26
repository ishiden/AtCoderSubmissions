import sys

input = sys.stdin.readline

def main():
    ans = 0
    n,x,t = map(int, input().split())
    ans = n//x
    if n%x != 0:
        ans += 1
    ans = ans * t

    print(ans)

if __name__ == '__main__':
    main()