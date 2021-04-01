import sys

input = sys.stdin.readline

def main():
    S = input().rstrip('\n')
    ans = 'x' * len(S)
    print(ans)

if __name__ == '__main__':
    main()