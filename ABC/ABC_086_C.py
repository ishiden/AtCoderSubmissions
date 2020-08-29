import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    n = int(input())
    now = [0,0]
    pt = 0
    for i in range(n):
        t, x, y = map(int, input().split())
        d = abs((x - now[0]) + (y - now[1]))
        if d > abs(t - pt) and (t - pt)%2 != d%2:
            ans = "No"
            break
        now = [x, y]
        pt = t
    print(ans)

if __name__ == '__main__':
    main()