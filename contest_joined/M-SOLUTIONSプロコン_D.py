import sys

input = sys.stdin.readline

def main():
    ans = 1000
    s = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = [""]*n
    for i in reversed(range(n)):
        if a[i]>a[i-1]:
            b[i]="sell"
        elif a[i]<=a[i-1]:
            b[i]="buy"
    if a[0] <= a[1]:
      b[0] = "buy"
    elif a[0] > a[1]:
      b[0] = "sell"
    for i in range(n):
        if b[i] == "sell" and (i==n-1 or b[i+1] != "sell"):
            ans += s*a[i]
            s = 0
        elif b[i] == "buy" and i != n-1 and b[i+1] != "buy":
            s += ans//a[i]
            ans -= ans//a[i]*a[i]

    print(ans)

if __name__ == '__main__':
    main()
