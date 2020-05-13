import sys

input = sys.stdin.readline

def main():
    ans = 0
    x = 0
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == 'I':
            x += 1
            ans = max(ans, x)
        else:
            x -= 1
    print(ans)

if __name__ == '__main__':
    main()