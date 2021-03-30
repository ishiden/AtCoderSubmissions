import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    ans = N
    while K > 0:
        tmp_s = sorted(list(str(ans)))
        tmp_g = tmp_s[::-1]
        ans = int(''.join(tmp_g)) - int(''.join(tmp_s))
        K -= 1
    print(ans)

if __name__ == '__main__':
    main()