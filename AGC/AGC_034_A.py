import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N, A, B, C, D = map(int, input().split())
    S = input()
    if '##' in S[A - 1:C] or '##' in S[B - 1:D]:
        ans = 'No'
    elif C > D and '...' not in S[B - 2:D + 1]:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()