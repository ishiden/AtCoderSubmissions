import sys

input = sys.stdin.readline

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X_sorted = sorted(X)
    s_m,  g_m = X_sorted[N//2 - 1], X_sorted[N//2]
    for x in X:
        if x <= s_m:
            print(g_m)
        else:
            print(s_m)

if __name__ == '__main__':
    main()