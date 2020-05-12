import sys

input = sys.stdin.readline

def main():
    ans = 0
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        x -= a[i]
        if x >= 0:
            ans += 1
        else:
            break
    if x>0:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()