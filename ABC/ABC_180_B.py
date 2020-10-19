import sys

input = sys.stdin.readline

def main():
    m, u, c = 0, 0, 0
    N = int(input())
    X = list(map(int, input().split()))
    for i in range(N):
        m += abs(X[i])
        u += X[i]**2
        c = max(c, abs(X[i]))
    print(m)
    print('{:.9}'.format(u**0.5))
    print(c)

if __name__ == '__main__':
    main()