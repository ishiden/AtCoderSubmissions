import sys

input = sys.stdin.readline

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if not 1 in a:
        print(-1)
        exit()
    f = a.index(1)
    c = 2
    ans = f-1
    for i in range(f,N):
        if a[i] == c:
            c += 1
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()