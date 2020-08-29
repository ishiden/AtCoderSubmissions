import sys

input = sys.stdin.readline

def main():
    ans = 10000
    s = input().rstrip('\n')
    t = input().rstrip('\n')
    lent = len(t)
    lens = len(s)
    tmp = 0
    for i in range(lens-lent+1):
        tmp = 0
        for j in range(lent):
            if s[i:i+lent][j] != t[j]:
                tmp += 1
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()