import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, A, B = map(int, input().split())
    for _ in range(N):
        s, d = input().rstrip('\n').split()
        d = int(d)
        if d < A:
            d = A
        elif d > B:
            d = B
        if s == 'East':
            ans += d
        else:
            ans -= d
    if ans > 0:
        ans = 'East ' + str(ans)
    elif ans < 0:
        ans = 'West ' + str(abs(ans))
    print(ans)

if __name__ == '__main__':
    main()