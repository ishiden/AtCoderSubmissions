import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    if N >= M:
        print(ans)
        exit()
    X.sort()
    dist = []
    for i in range(M-1):
        dist.append(X[i+1] - X[i])
    dist.sort()
    p = M - N
    ans = sum(dist[:p])
    print(ans)

if __name__ == '__main__':
    main()