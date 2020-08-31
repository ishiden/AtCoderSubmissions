import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    s = []
    for i in range(n):
        t = int(input())
        ans += t
        s.append(t)
    s.sort()

    if ans%10 == 0:
        for i in range(n):
            if s[i]%10 != 0:
                ans -= s[i]
                break
    print(ans if ans%10 != 0: 0)

if __name__ == '__main__':
    main()