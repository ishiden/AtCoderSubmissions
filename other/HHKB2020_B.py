import sys

input = sys.stdin.readline

def main():
    ans = 0
    H, W = map(int, input().split())
    cells = []
    for _ in range(H):
        cells.append(list(input().rstrip('\n')))
    for i in range(H):
        for j in range(W):
            if cells[i][j] == '.':
                if i + 1 <= H - 1 and cells[i + 1][j] == '.':
                    ans += 1
                if j + 1 <= W - 1 and cells[i][j + 1] == '.':
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()