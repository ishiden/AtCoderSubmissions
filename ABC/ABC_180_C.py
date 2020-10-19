import sys

input = sys.stdin.readline

def make_divisors(n):
    lower_divisors , upper_divisors = '', ''
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors += str(i) + '\n'
            if i != n // i:
                upper_divisors = str(n//i) + '\n' + upper_divisors
        i += 1
    return lower_divisors + upper_divisors

def main():
    N = int(input())
    ds = make_divisors(N)
    print(ds)

if __name__ == '__main__':
    main()