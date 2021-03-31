import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    l = []
    for i in range(N):
        A, B = map(int, input().split())
        l.append([A, B])
    for i in l[::-1]:
        tmp = i[1] - (i[0] + ans) % i[1] if (i[0] + ans) % i[1] != 0 else 0
        ans += tmp

    print(ans)

if __name__ == '__main__':
    main()