import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    pl = []
    for  i in range(N):
        x, y = map(int, input().split())
        pl += [x, y]
    for i in range(N - 1):
        for j in range(i + 1, N):
            g = (pl[j][1] - pl[i][1]) / (pl[i][0] - pl[j][0])
            if -1 <= g and g <= 1:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()