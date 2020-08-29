import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    d,t,s = map(int, input().split())
    if s*t >= d:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()