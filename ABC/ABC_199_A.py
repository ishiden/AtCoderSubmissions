import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    A, B, C = map(int, input().split())
    if A**2 + B**2 >= C**2:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()