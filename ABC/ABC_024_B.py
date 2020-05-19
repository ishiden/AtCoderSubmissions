import sys

input = sys.stdin.readline

def main():
    N, T = map(int, input().split())
    ans = T
    t = []
    for i in range(N):
        t.append(int(input()))
    for i in range(N-1):
        if t[i]+T < t[i+1]:
            ans += T
        else:
            ans += t[i+1]-t[i]
    print(ans)

if __name__ == '__main__':
    main()