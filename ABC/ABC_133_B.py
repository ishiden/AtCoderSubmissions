import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, D = map(int, input().split())
    p = []
    for i in range(N):
        p.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(i, N):
            temp = 0
            for k in range(D):
                temp += (p[i][k]-p[j][k])**2
            if temp != 0 and float.is_integer(temp**0.5):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()