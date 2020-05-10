import sys

input = sys.stdin.readline

def main():
    ans = 0
    n, m ,x = map(int, input().split())
    a = list(map(int, input().split()))
    l = [0]*(n+1)
    for ai in a:
        l[ai] = 1
    ans = min(sum(l[:x]), sum(l[x:]))
    print(ans)

if __name__ == '__main__':
    main()