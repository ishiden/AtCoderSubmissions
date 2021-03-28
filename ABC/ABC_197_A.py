import sys

input = sys.stdin.readline

def main():
    s = input().rstrip('\n')
    print(s[1:]+s[:1])

if __name__ == '__main__':
    main()