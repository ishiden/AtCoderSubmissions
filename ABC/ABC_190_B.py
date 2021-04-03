import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if S > X and D < Y:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()