import sys

input = sys.stdin.readline

def main():
    ans = 0
    H,W,K = map(int, input().split())
    l = []
    for _ in range(H):
        l.append(list(input().rstrip('\n')))
    for i in range(2**H):
        for j in range(2**W):
            b = 0
            for h in range(H):
                for w in range(W):
                    if i>>h & 1 and j>>w & 1 and l[h][w] == '#':
                        b += 1
            if b == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()