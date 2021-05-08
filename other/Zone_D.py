import sys

input = sys.stdin.readline

def main():
    ans = ''
    S = input().rstrip('\n')
    r = False
    for i in range(len(S)):
        if S[i] == 'R':
            r = not r
        else:
            if r:
                ans = S[i] + ans
            else:
                ans += S[i]
        if len(ans) >= 2:
            if ans[0] == ans[1] and r:
                ans = ans[2:]
            elif ans[-1] == ans[-2] and not r:
                ans = ans[:-2]
    if r:
        ans = ans[::-1]
    print(ans)

if __name__ == '__main__':
    main()