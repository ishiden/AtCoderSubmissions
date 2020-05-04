import sys

input = sys.stdin.readline

def main():
    ans = 0
    n,m = map(int, input().split())
    ma = [0]*n
    hl = list(map(int, input().split()))
    for i in range(m):
        a,b = map(int, input().split())
        ma[a-1] = max(ma[a-1], hl[b-1])
        ma[b-1] = max(ma[b-1], hl[a-1])
    for i in range(n):
        if hl[i] > ma[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()