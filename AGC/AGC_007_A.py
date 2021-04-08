import sys

input = sys.stdin.readline

def main():
    ans = 'Possible'
    l = 0
    H, W = map(int, input().split())
    for i in range(H):
        S = input().rstrip('\n')
        if '#' in S[:l]:
            ans = 'Impossible'
            break
        for j in range(l, W):
            if S[j] != '#':
                l = j - 1
                break
        if '#' in S[l + 1:W]:
            ans = 'Impossible'
            break

    print(ans)

if __name__ == '__main__':
    main()