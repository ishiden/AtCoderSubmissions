import sys

input = sys.stdin.readline

def main():
    ans = []
    N, K, S = map(int, input().split())
    for _ in range(K):
        ans.append(S)
    other = 1 if S == 10 ** 9 else S + 1
    for _ in range(K, N):
        ans.append(other)
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()