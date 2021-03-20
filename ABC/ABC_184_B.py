import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, X = map(int, input().split())
    S = input().rstrip('\n')
    for s in S:
        if s == 'x':
            X = max(0, X-1)
        else:
            X += 1
    print(X)

if __name__ == '__main__':
    main()