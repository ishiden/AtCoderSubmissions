import sys

input = sys.stdin.readline

def popcount(n):
    return bin(n).count('1')

def calc(n):
    cnt = 0
    while n != 0:
        n %= popcount(n):
        cnt += 1
    return cnt

def main():
    ans = 0
    n = int(input())
    x = input().rstrip('\n')
    popx = x.count('1')
    x = int(x, 2)
    x_p = x%(popx+1)
    x_m = x%(popx-1) if popx-1 > 0 else float('inf')
    for i, v in enumerate(s):
        if v == '0':
            x = x_p



    print(ans)

if __name__ == '__main__':
    main()