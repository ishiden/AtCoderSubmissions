import sys

input = sys.stdin.readline

def main():
    ans = 0
    if input().rstrip('\n') == 'Y':
        print(input().rstrip('\n').upper())
    else:
        print(input().rstrip('\n'))

if __name__ == '__main__':
    main()