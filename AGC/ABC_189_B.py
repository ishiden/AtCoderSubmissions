import sys

input = sys.stdin.readline

def main():
    ans = -1
    alcohol = 0
    N, X = map(int, input().split())
    X *= 100
    for i in range(N):
        V, P = map(int, input().split())
        alcohol += V * P
        if alcohol > X:
            ans = i + 1
            break
    print(ans)

if __name__ == '__main__':
    main()