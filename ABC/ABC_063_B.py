import sys

input = sys.stdin.readline

def main():
    ans = 'no'
    s = input()
    if len(s) == len(set(s)):
        ans = 'yes'
    print(ans)

if __name__ == '__main__':
    main()