import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K > N:
        ans = 0
    else:
        ans = sum(H[K:])

    print(ans)

if __name__ == '__main__':
    main()