import sys

input = sys.stdin.readline

def main():
    ans = 0
    K = int(input())
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            if i * j <= K:
                ans += K // (i * j)
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()