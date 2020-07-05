import sys

input = sys.stdin.readline

def main():
    S = input().rstrip('\n')
    print(str.capitalize(S))

if __name__ == '__main__':
    main()