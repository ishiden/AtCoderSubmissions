import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    A, B = map(int, input().split())
    S = input()
    if S[A] == '-' and S.count('-') == 1:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()