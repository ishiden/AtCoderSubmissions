import sys

input = sys.stdin.readline

def main():
    ans = ''
    S = input().rstrip('\n')
    for i in range(len(S)):
        if S[i] == '6':
            ans += '9'
        elif S[i] == '9':
            ans += '6'
        else:
            ans += S[i]
    print(ans[::-1])

if __name__ == '__main__':
    main()