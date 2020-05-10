import sys

input = sys.stdin.readline

def main():
    ans = 0
    a, b, c, k = map(int, input().split())
    if a >= k:
        ans = k
    else:
        ans = a
        if b < (k-a):
            ans += -1*(k-a-b)

    print(ans)

if __name__ == '__main__':
    main()