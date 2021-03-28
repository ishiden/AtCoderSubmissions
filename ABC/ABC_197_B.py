import sys

input = sys.stdin.readline

def main():
    ans = 0
    s = []
    H, W, Y, X = map(int, input().split())
    for i in range(H):
        s.append(input().rstrip('\n'))
    for h in range(Y - 1):
        if s[h][X - 1] == '.':
            ans += 1
        else:
            ans = 0
    for h in range(Y - 1, H):
        if s[h][X - 1] == '.':
            ans += 1
        else:
            break
    tmp = 0
    for w in range(X - 1):
        if s[Y - 1][w] == '.':
            tmp += 1
        else:
            tmp = 0
    for w in range(X - 1, W):
        if s[Y - 1][w] == '.':
            tmp += 1
        else:
            break
    if s[Y - 1][X - 1] == '.':
        ans -= 1

    print(ans + tmp)

if __name__ == '__main__':
    main()