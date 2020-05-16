import sys

input = sys.stdin.readline

def calc(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def main():
    ans = 0
    N, A, B = map(int, input().split())
    for i in range(1, N+1):
        temp = calc(i)
        if A <= temp <= B:
            ans += i

    print(ans)

if __name__ == '__main__':
    main()