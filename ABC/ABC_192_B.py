import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    S = input().rstrip('\n')
    if S[1::2] != S[1::2].upper():
        ans = 'No'
    if ans == 'Yes' and S[::2] != S[::2].lower():
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()