import sys

input = sys.stdin.readline

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors

def main():
    ans = []
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        ans += make_divisors(i)
    ans.sort(reverse=True)
    tmp = ans[0]
    for i in range(1, len(ans)):
        if tmp == ans[i]:
            ans = ans[i]
            break
        else:
            tmp = ans[i]
    print(ans)

if __name__ == '__main__':
    main()