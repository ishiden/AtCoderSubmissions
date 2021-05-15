import sys

input = sys.stdin.readline

def main():
    f, s = 0, 0
    fn, sn = '', ''
    N = int(input())
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if T > f:
            s = f
            sn = fn
            f = T
            fn = S
        elif T > s:
            sn = S
            s = T

    print(sn)

if __name__ == '__main__':
    main()