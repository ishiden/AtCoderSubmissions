import sys
import math

input = sys.stdin.readline

def main():
    ans = 1
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    for i in range(N):
        ans = math.gcd(ans, abs(x[i]-x[i+1]))
    print(ans)

if __name__ == '__main__':
    main()