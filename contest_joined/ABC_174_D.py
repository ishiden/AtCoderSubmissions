import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    c = input().rstrip('\n')
    r = c.count('R')
    s = 0
    for i in range(n):
        if c[i]=='R':
            w = c[s:i].count('W')
            ans += min(w,r)
            s = i
            r -= w+1
            if r <= 0:
                break
    print(ans)

if __name__ == '__main__':
    main()
