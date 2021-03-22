import sys

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    for i in range(len(S)):
        if S[i] == 'U':
            ans += len(S[i + 1:]) + len(S[:i]) * 2
        else:
            ans += len(S[i + 1:]) * 2 + len(S[:i])

    print(ans)

if __name__ == '__main__':
    main()