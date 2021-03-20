import sys

input = sys.stdin.readline

def main():
    ans = 10**9
    s = input().rstrip('\n')
    for c in set(s):
        M = 0
        tmp = s.split(c)
        for sec in tmp:
            M = max(M, len(sec))
        ans = min(M, ans)
    print(ans)

if __name__ == '__main__':
    main()