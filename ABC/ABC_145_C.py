import sys

input = sys.stdin.readline

def calc(p1, p2):
    return ((((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)))**0.5


def main():
    ans = 0
    N = int(input())
    l = [list(map(int, input().split())) for _ in range(N)]
    r = []
    for i in range(N-1):
        for j in range(i+1, N):
            r.append(calc(l[i], l[j]))
    ans = sum(r)*2/N
    print(f'{ans:.8f}')

if __name__ == '__main__':
    main()